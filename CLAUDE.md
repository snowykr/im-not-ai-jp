# im-not-ai-jp

Japanese Fast Path skill for reducing AI-like prose while preserving meaning.

## Project Shape

```
im-not-ai-jp/
├── .claude-plugin/plugin.json
├── .claude/skills/
│   ├── humanize-japanese/
│   ├── humanize/
│   └── humanize-redo/
├── codex/skills/humanize-japanese/
├── commands/
│   ├── humanize-japanese.toml
│   ├── humanize.toml
│   └── humanize-redo.toml
├── legacy/upstream-korean/
├── install.sh
├── uninstall.sh
├── README.md
├── INSTALL.md
└── NOTICE
```

## Rules

- Preserve facts, names, numbers, dates, and direct quotes.
- Keep genre and register.
- Do not reuse the Korean taxonomy as the Japanese taxonomy.
- Keep upstream Korean material in `legacy/upstream-korean/` for attribution and reference only.
- Install only `humanize-japanese`, `humanize`, and `humanize-redo` from `.claude/skills/`.
- Keep release and marketplace language aligned with the Japanese package state.

## Upstream Policy

`epoko77-ai/im-not-ai` may be used as a read-only source for infrastructure cherry-picks. Use `git cherry-pick -x` when importing a patch so the source commit is traceable.

Japanese rules, examples, prompts, and evaluation data are maintained independently in this repository.
