---
name: humanize-japanese
description: AI(ChatGPT, Claude, Geminiなど)が生成した日本語の下書きから、機械的な丁寧体、翻訳調、定型的な説明文、過剰な箇条書きや結論表現を減らし、意味を保ったまま自然な日本語に整える。トリガー: "AIっぽさを消して", "日本語を自然にして", "翻訳調を直して", "人が書いたように", "humanize Japanese"。
---

# Humanize Japanese — Fast Path (Codex)

Japanese-only Fast Path for reducing AI-like prose while preserving meaning.

## Rules

1. Preserve facts, claims, numbers, dates, proper nouns, citations, and direct quotes.
2. Keep the original genre and register.
3. Read `references/quick-rules.md` from this skill directory before rewriting.
4. Rewrite only spans that match the Japanese quick rules.
5. Do not add new claims or examples.
6. If the input is not primarily Japanese, explain that this skill handles Japanese text only.

## Output

Write `_workspace/{YYYY-MM-DD-NNN}/final.md` with the rewritten text and a compact HTML comment summary containing:

- rough change rate
- categories addressed
- self-check result
- 3 to 5 representative before/after highlights

Reply briefly with status, key categories, and the `final.md` path.
