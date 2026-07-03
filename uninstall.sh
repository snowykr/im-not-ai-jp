#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_HOME="${CLAUDE_HOME:-$HOME/.claude}"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
DRYRUN=0

case "${1:-}" in
  --dry-run) DRYRUN=1 ;;
  -h|--help) echo "Usage: ./uninstall.sh [--dry-run]"; exit 0 ;;
  "") ;;
  *) echo "unknown arg: $1" >&2; exit 2 ;;
esac

remove_if_ours() {
  local dest="$1"
  shift
  if [ -L "$dest" ]; then
    local actual
    actual="$(readlink "$dest")"
    local src
    for src in "$@"; do
      if [ "$actual" = "$src" ]; then
        echo "+ rm $dest"; [ "$DRYRUN" = 1 ] || rm "$dest"
        return 0
      fi
    done
  fi
  if [ -e "$dest" ]; then
    echo "skip (not managed by this repository): $dest"
  fi
  return 0
}

remove_codex_plugin_if_installed() {
  if ! command -v codex >/dev/null 2>&1; then
    return 0
  fi

  if [ "$DRYRUN" = 1 ]; then
    echo "+ codex plugin remove im-not-ai-codex@im-not-ai-jp (dry-run)"
    return 0
  fi

  codex plugin remove im-not-ai-codex@im-not-ai-jp --json >/dev/null 2>&1 \
    && echo "removed: Codex plugin (im-not-ai-codex@im-not-ai-jp)" \
    || echo "  (Codex plugin is not installed or was already removed)"
}

for s in humanize-japanese humanize humanize-redo; do
  remove_if_ours "$CLAUDE_HOME/skills/$s" "$REPO/.claude/skills/$s"
done
remove_codex_plugin_if_installed
remove_if_ours "$CODEX_HOME/skills/humanize-japanese" \
  "$REPO/plugins/im-not-ai-codex/skills/humanize-japanese" \
  "$REPO/codex/skills/humanize-japanese"
for a in "$REPO/agents"/*.md; do
  remove_if_ours "$CLAUDE_HOME/agents/$(basename "$a")" "$a"
done

# ---- Gemini CLI ----
if command -v gemini >/dev/null 2>&1; then
  echo "Trying to remove the Gemini extension..."
  if [ "$DRYRUN" = 1 ]; then
    echo "+ gemini extensions uninstall im-not-ai-jp (dry-run)"
  else
    gemini extensions uninstall im-not-ai-jp 2>/dev/null && echo "removed: Gemini extension (im-not-ai-jp)" \
      || echo "  (Gemini extension is not installed or was already removed)"
  fi
fi

echo "アンインストール完了。(.bak.* バックアップと --copy で作成したコピーは保持されます)"
