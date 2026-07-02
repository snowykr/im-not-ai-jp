---
name: humanize-japanese
version: "0.1.0"
description: AI(ChatGPT, Claude, Geminiなど)が生成した日本語の下書きから、機械的な丁寧体、翻訳調、定型的な説明文、過剰な箇条書きや結論表現を減らし、意味を保ったまま自然な日本語に整える。トリガー: "AIっぽさを消して", "日本語を自然にして", "翻訳調を直して", "人が書いたように", "humanize Japanese"。
---

# Humanize Japanese — Fast Path

AI生成の日本語テキストを、意味を変えずに文体、リズム、表現だけ整える。

## Principles

1. **意味を変えない**: 事実、主張、数値、日付、固有名詞、引用は保持する。
2. **検出根拠を持つ**: `references/quick-rules.md`に対応する箇所を中心に直す。
3. **ジャンルを保つ**: ビジネス文書、ブログ、レポート、メールなどの用途を変えない。
4. **過剰に崩さない**: 丁寧体そのものを悪としない。均一すぎる調子だけを緩める。
5. **書き換えすぎない**: 変更率が高い場合は、変更理由を明示して保守的に止める。

## Process

1. Read `references/quick-rules.md`.
2. Identify the input text or read the provided `.txt` / `.md` file path.
3. If the text is not primarily Japanese, explain that this skill handles Japanese text only.
4. Estimate genre from the first 300 characters unless the user provided one.
5. Detect AI-like spans using the quick-rule categories.
6. Rewrite only the relevant spans while preserving meaning and register.
7. Self-check:
   - no factual drift
   - no deleted names, numbers, dates, or quotes
   - no genre drift
   - no excessive casualization
   - no added claims
8. Write the result to `_workspace/{YYYY-MM-DD-NNN}/final.md` and include a compact summary comment at the end.
9. Respond with a short status, the main categories fixed, and the path to `final.md`.

## Options

Natural-language options may appear at the end of the request:

- `ジャンル: ビジネス|ブログ|レポート|メール|公的`
- `強度: 控えめ|標準|強め`
- `最小深刻度: S1|S2|S3`

## References

- `references/quick-rules.md` — current compact Japanese Fast Path rules

## Status

This is the initial Japanese split. The strict multi-agent taxonomy from the Korean upstream project is intentionally not reused as-is.
