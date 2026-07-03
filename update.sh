#!/usr/bin/env bash
# im-not-ai-jp - check for repository updates and re-apply install.sh.
# Symlink installs usually update after pull, but re-running install.sh keeps
# new skill files and layout changes connected.
#
# Usage:
#   ./update.sh            check updates, then fast-forward and reinstall
#   ./update.sh --check    check only; up-to-date=0, update available=10
#   other arguments pass through to install.sh, e.g. ./update.sh --codex-only
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
g() { git -C "$REPO" "$@"; }

usage() { sed -n '2,11p' "$0"; }

CHECK_ONLY=0
ARGS=()
for a in "$@"; do
  case "$a" in
    --check) CHECK_ONLY=1 ;;
    -h|--help) usage; exit 0 ;;
    *) ARGS+=("$a") ;;
  esac
done

g rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "not a git repository: $REPO"; exit 2; }

ver() { grep -o '"version"[[:space:]]*:[[:space:]]*"[^"]*"' "$REPO/.claude-plugin/plugin.json" 2>/dev/null \
          | head -1 | grep -o '[0-9][0-9.]*' \
       || grep -o '"version"[[:space:]]*:[[:space:]]*"[^"]*"' "$REPO/gemini-extension.json" 2>/dev/null \
          | head -1 | grep -o '[0-9][0-9.]*' \
       || echo "?"; }

UPSTREAM="$(g rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || echo origin/main)"
UP_REMOTE="${UPSTREAM%%/*}"
echo "checking for updates... (tracking: $UPSTREAM)"
g fetch --quiet "$UP_REMOTE" || { echo "fetch failed; check network and remote settings."; exit 2; }

LOCAL="$(g rev-parse HEAD)"
REMOTE="$(g rev-parse "$UPSTREAM" 2>/dev/null || true)"
[ -z "$REMOTE" ] && { echo "cannot find upstream branch: $UPSTREAM"; exit 2; }
BASE="$(g merge-base HEAD "$UPSTREAM" 2>/dev/null || echo "")"

if [ "$LOCAL" = "$REMOTE" ]; then
  echo "already up to date - v$(ver) ($(g rev-parse --short HEAD))."
  exit 0
elif [ "$BASE" = "$REMOTE" ]; then
  echo "local branch is ahead of upstream; no update to apply."
  exit 0
elif [ "$BASE" != "$LOCAL" ]; then
  echo "local branch diverged from upstream; manual merge is required."
  echo "  local=$(g rev-parse --short HEAD)  upstream=$(g rev-parse --short "$UPSTREAM")"
  exit 1
fi

BEHIND="$(g rev-list --count "HEAD..$UPSTREAM")"
echo "update available: $BEHIND commit(s) ($UPSTREAM)"
g --no-pager log --oneline "HEAD..$UPSTREAM" 2>/dev/null | head -10 | sed 's/^/    /'

if [ "$CHECK_ONLY" = 1 ]; then
  echo "(--check: not applying changes. Run ./update.sh to update.)"
  exit 10
fi

OLD="$(ver)"
echo "fast-forward pull..."
g pull --ff-only
echo "re-applying install.sh..."
"$REPO/install.sh" ${ARGS[@]+"${ARGS[@]}"}
echo "update complete: v$OLD -> v$(ver)."
