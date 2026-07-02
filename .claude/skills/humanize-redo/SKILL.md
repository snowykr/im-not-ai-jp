---
name: humanize-redo
description: 直近のHumanize Japanese結果を、カテゴリ、段落、強度の指定に合わせてもう一度整える。トリガー — "/humanize-redo"。
argument-hint: "[調整指示 — 例: \"翻訳調だけ\" \"この段落だけ\" \"控えめに\"]"
disable-model-invocation: true
---

# /humanize-redo

直近の`_workspace/{run_id}/final.md`を探し、ユーザーの調整指示に合わせて再編集する。

## Input

$ARGUMENTS

## Behavior

1. Find the latest `_workspace/YYYY-MM-DD-*/final.md` or `01_input.txt`.
2. If no previous run exists, tell the user to start with `/humanize-japanese` or `/humanize`.
3. Parse the adjustment:
   - category only, such as translation-like wording or polite-style monotony
   - paragraph only
   - lower or higher rewrite intensity
   - revert a specific change
4. Preserve meaning, names, numbers, dates, and quotes.
5. Write a new result and return a compact comparison.

## Limit

Do not invent a strict multi-agent Japanese pipeline. This initial split only provides the Japanese Fast Path.

## Reference

- `humanize-japanese/references/quick-rules.md`
