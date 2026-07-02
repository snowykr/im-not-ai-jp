# im-not-ai-jp

Japanese adaptation of `epoko77-ai/im-not-ai` for making AI-generated Japanese drafts read less templated, less translation-like, and more naturally authored.

This project is **not** a direct Japanese translation of the Korean rule set. It keeps the original repository structure, installer approach, and multi-CLI packaging as the starting point, but the Japanese detection taxonomy, rewriting rules, prompts, and examples are maintained independently here.

## Attribution

This repository began as an independent mirror-based adaptation of [`epoko77-ai/im-not-ai`](https://github.com/epoko77-ai/im-not-ai), licensed under the MIT License.

- Original copyright notice is preserved in [`LICENSE`](LICENSE).
- Project-level derivation is documented in [`NOTICE`](NOTICE).
- Legacy Korean upstream material is retained under [`legacy/upstream-korean/`](legacy/upstream-korean/) for reference only and is not installed by default.

## Current Scope

`im-not-ai-jp` focuses on Japanese AI-writing tells such as:

- uniform polite style and monotone sentence endings
- overused explanation templates like `重要です`, `必要があります`, `〜と言えるでしょう`
- translation-like structures such as `〜することができます`, `〜において`, `〜を通じて`
- mechanical headings, bullet rhythm, and conclusion pivots
- unnecessary emphasis, balanced-but-empty framing, and generic value-claim language

The first public milestone is a Fast Path skill for Claude Code, Codex CLI, and Gemini CLI. The stricter multi-agent Japanese taxonomy is intentionally separate future work.

## Visibility Policy

This repository stays **private during incubation**. It should only be made public after the Japanese taxonomy, examples, install flow, and project documentation are strong enough to represent an independent public project.

Until then, treat `snowykr/im-not-ai-jp` as a private working repository, not a public fork, marketplace package, or announced release.

## Install

Clone this independent repository:

```bash
git clone https://github.com/snowykr/im-not-ai-jp.git
cd im-not-ai-jp
./install.sh
```

Installed entry points:

- Claude Code: `/humanize-japanese`
- Codex CLI: `$humanize-japanese`
- Gemini CLI: `/humanize-japanese`

Single-tool installs:

```bash
./install.sh --claude-only
./install.sh --codex-only
./install.sh --gemini-only
```

Remove symlink installs:

```bash
./uninstall.sh
```

## Upstream Policy

The original project remains useful as a read-only upstream for common infrastructure fixes. This project may cherry-pick installer, packaging, CI, or documentation infrastructure patches from `epoko77-ai/im-not-ai` with attribution, preferably using:

```bash
git cherry-pick -x <upstream-commit>
```

Japanese language rules, examples, prompts, and evaluation material should be developed independently in this repository.

## Status

This is the initial project split. The Japanese quick rules are intentionally compact and should be expanded with real Japanese corpora, model outputs, and reviewer feedback before any strict detection claims are made.
