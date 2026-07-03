# Install

`im-not-ai-jp` installs a Japanese Fast Path skill into supported local AI coding CLIs. Codex users should prefer the native Codex plugin path; direct skill symlinks remain as a compatibility path.

Use `main` until the first Japanese release tag is published. After `jp-v0.1.0` exists, pin installs to that tag for a stable snapshot.

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
- `humanize-japanese`, `humanize`, and `humanize-redo` skills

Use in a new Claude Code session:

```text
/humanize-japanese
```

## Codex CLI

Recommended native plugin install:

```bash
git clone https://github.com/snowykr/im-not-ai-jp.git
cd im-not-ai-jp
codex plugin marketplace add .
codex plugin add im-not-ai-codex@im-not-ai-jp
```

Use in Codex:

```text
$humanize-japanese
```

Normal calls use Fast default mode. Strict precision runs only when the user explicitly asks for `strict`, `精密`, `subagent`, or `parallel review`; the plugin then follows a Codex subagent workflow and keeps pasted text as data rather than instructions.

Compatibility path for environments without `codex plugin`:

```bash
./install.sh --codex-only
```

Installs:

- `~/.codex/skills/humanize-japanese` linked to `plugins/im-not-ai-codex/skills/humanize-japanese`

Direct skill usage is the same:

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
codex plugin marketplace add .
codex plugin add im-not-ai-codex@im-not-ai-jp
./install.sh
```

Use `./update.sh --check` to inspect whether the configured tracking branch has newer commits.

## Uninstall

```bash
./uninstall.sh
```

The uninstall script removes the native Codex plugin install and symlinks that point back to this repository. It does not remove copied installs or backups.
