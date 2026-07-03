---
name: humanize
description: AIが生成した日本語テキストを自然に整える入口コマンド。humanize-japanese Fast Pathを実行する。トリガー — "/humanize"。
argument-hint: "[整える日本語テキストまたはファイルパス]"
disable-model-invocation: true
---

# /humanize

`humanize-japanese` skillを発動し、渡された日本語テキストまたはファイルを整える。

## Input

$ARGUMENTS

## Behavior

1. If the argument is empty, ask the user to provide Japanese text.
2. If the argument is a `.txt` or `.md` path, read the file.
3. If the argument is text, use it as the input.
4. Follow `humanize-japanese` Fast Path rules.
5. Return a compact status, the categories addressed, representative before/after examples, and the `final.md` path.

## Options

- `ジャンル: ビジネス|ブログ|レポート|メール|公的`
- `強度: 控えめ|標準|強め`
- `カテゴリ: register_monotony|translationese_posteditese|readability_texture|honorific_politeness_safety|genre_preset|stylometric_diagnostics`
- `プロファイル: easy_japanese`

## Reference

- `humanize-japanese/references/quick-rules.md`
