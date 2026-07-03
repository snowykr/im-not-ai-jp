#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"

MODE=symlink          # symlink | copy
DO_CLAUDE=auto        # auto | yes | no
DO_CODEX=auto
DO_GEMINI=auto
FORCE=0
DRYRUN=0
TS="$(date +%Y%m%d-%H%M%S)"

print_help() {
  cat <<'H'
Usage: ./install.sh [options]

  Detect installed CLIs and install the humanize-japanese skill globally.
  Claude: ~/.claude/skills/{humanize-japanese,humanize,humanize-redo}
  Codex : ~/.codex/skills/humanize-japanese (native plugin skill source)
  Gemini: gemini extensions link (gemini-extension.json + GEMINI.md + commands/)

Options:
  --copy          Copy instead of symlink. Reference symlinks are materialized.
                  Copied installs are preserved by uninstall.sh.
  --claude-only   Install Claude targets only.
  --codex-only    Install Codex targets only.
  --gemini-only   Install Gemini targets only.
  --no-gemini     Skip Gemini and install only Claude/Codex targets.
  --force         Back up existing files/directories as .bak.<ts> and replace them.
  --dry-run       Print planned changes without modifying files.
  -h, --help      Show this help.

Env overrides: CLAUDE_HOME(default ~/.claude), CODEX_HOME(default ~/.codex)
H
}

while [ $# -gt 0 ]; do
  case "$1" in
    --copy) MODE=copy ;;
    --claude-only) DO_CLAUDE=yes; DO_CODEX=no; DO_GEMINI=no ;;
    --codex-only) DO_CLAUDE=no; DO_CODEX=yes; DO_GEMINI=no ;;
    --gemini-only) DO_CLAUDE=no; DO_CODEX=no; DO_GEMINI=yes ;;
    --no-gemini) DO_GEMINI=no ;;
    --force) FORCE=1 ;;
    --dry-run) DRYRUN=1 ;;
    -h|--help) print_help; exit 0 ;;
    *) echo "unknown arg: $1" >&2; print_help; exit 2 ;;
  esac
  shift
done

run() { echo "+ $*"; [ "$DRYRUN" = 1 ] || "$@"; }

has_claude_target() {
  command -v claude >/dev/null 2>&1 || [ -d "$CLAUDE_HOME" ]
}

has_codex_target() {
  command -v codex >/dev/null 2>&1 || [ -d "$CODEX_HOME" ]
}

prepare_target() {
  local dest="$1" src="$2"
  if [ -L "$dest" ]; then
    if [ "$(readlink "$dest")" = "$src" ]; then
      echo "ok (already linked): $dest"; return 1
    fi
    run mv "$dest" "$dest.bak.$TS"
  elif [ -e "$dest" ]; then
    if [ "$FORCE" != 1 ]; then
      echo "refuse: $dest already exists (use --force to back it up and replace it, or use --copy)"; return 2
    fi
    run mv "$dest" "$dest.bak.$TS"
  fi
  return 0
}

install_one() {
  local src="$1" dest="$2"
  run mkdir -p "$(dirname "$dest")"
  local rc=0
  prepare_target "$dest" "$src" || rc=$?
  [ "$rc" = 1 ] && return 0
  [ "$rc" = 2 ] && return 1
  case "$MODE" in
    symlink) run ln -s "$src" "$dest" ;;
    copy)    run cp -RL "$src" "$dest" ;;
  esac
  echo "installed: $dest"
}

# ---- Claude ----
if [ "$DO_CLAUDE" != no ] && { [ "$DO_CLAUDE" = yes ] || has_claude_target; }; then
  echo "== Claude Code =="
  run mkdir -p "$CLAUDE_HOME/skills"
  for s in humanize-japanese humanize humanize-redo; do
    install_one "$REPO/.claude/skills/$s" "$CLAUDE_HOME/skills/$s"
  done
else
  echo "== Claude Code: skipped (claude or $CLAUDE_HOME not detected; use --claude-only to force) =="
fi

# ---- Codex ----
if [ "$DO_CODEX" != no ] && { [ "$DO_CODEX" = yes ] || has_codex_target; }; then
  echo "== Codex =="
  run mkdir -p "$CODEX_HOME/skills"
  install_one "$REPO/plugins/im-not-ai-codex/skills/humanize-japanese" "$CODEX_HOME/skills/humanize-japanese"
else
  echo "== Codex: skipped (codex or $CODEX_HOME not detected; use --codex-only to force) =="
fi

# ---- Gemini CLI ----
if [ "$DO_GEMINI" != no ] && { [ "$DO_GEMINI" = yes ] || command -v gemini >/dev/null 2>&1; }; then
  echo "== Gemini CLI =="
  if [ "$DRYRUN" = 1 ]; then
    echo "+ gemini extensions link $REPO (dry-run)"
  else
    echo "Running gemini extensions link \"$REPO\"..."
    echo "Y" | gemini extensions link "$REPO" 2>/dev/null && echo "installed: Gemini extension (im-not-ai-jp)" \
      || echo "  (already registered, or manual registration is required: gemini extensions link $REPO)"
  fi
else
  echo "== Gemini CLI: skipped (gemini not detected; use --gemini-only to force) =="
fi

echo ""
echo "Done (mode=$MODE)."
echo "  Claude: use /humanize-japanese (or /humanize) in a new session"
echo "  Codex : \$humanize-japanese"
echo "  Gemini: use /humanize-japanese (or /humanize) in a new session"
echo "  Update: ./update.sh · Uninstall: ./uninstall.sh"
exit 0
