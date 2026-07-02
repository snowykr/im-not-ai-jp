# Install

`im-not-ai-jp` installs a Japanese Fast Path skill into supported local AI coding CLIs.

```bash
git clone https://github.com/snowykr/im-not-ai-jp.git
cd im-not-ai-jp
./install.sh
```

## Claude Code

```bash
./install.sh --claude-only
```

Installs:

- `~/.claude/skills/humanize-japanese`
- supporting agents from `agents/`

Use in a new Claude Code session:

```text
/humanize-japanese
```

## Codex CLI

```bash
./install.sh --codex-only
```

Installs:

- `~/.codex/skills/humanize-japanese`

Use in Codex:

```text
$humanize-japanese
```

## Gemini CLI

```bash
./install.sh --gemini-only
```

Links this repository as a Gemini extension. Use in a new Gemini session:

```text
/humanize-japanese
```

## Options

| Option | Meaning |
| --- | --- |
| `--copy` | Copy files instead of creating symlinks. |
| `--claude-only` | Install only Claude Code files. |
| `--codex-only` | Install only Codex files. |
| `--gemini-only` | Install only Gemini extension files. |
| `--no-gemini` | Install Claude/Codex only. |
| `--force` | Back up conflicting files before replacing them. |
| `--dry-run` | Print planned actions without changing files. |

Environment overrides:

- `CLAUDE_HOME`, default `~/.claude`
- `CODEX_HOME`, default `~/.codex`

## Update

This repository is independent. `origin` should normally point to `snowykr/im-not-ai-jp`; `upstream` may point to `epoko77-ai/im-not-ai` only for selective infrastructure cherry-picks.

For this repo's own updates:

```bash
git pull --ff-only
./install.sh
```

Use `./update.sh --check` to inspect whether the configured tracking branch has newer commits.

## Uninstall

```bash
./uninstall.sh
```

The uninstall script removes only symlinks that point back to this repository. It does not remove copied installs or backups.
