# im-not-ai-jp — Gemini CLI Extension

Fast Path extension for reducing AI-like Japanese prose while preserving meaning.

## Commands

- `/humanize-japanese [text]`
- `/humanize [text]`
- `/humanize-redo [adjustment]`

## Principles

1. Preserve facts, claims, numbers, dates, proper nouns, citations, and direct quotes.
2. Keep the source genre and register.
3. Change only spans that match the Japanese quick-rule taxonomy. Each match is
   a rewrite cue, not authorship proof.
4. Avoid making formal Japanese unnecessarily casual.
5. Do not add claims, examples, or rhetorical flourishes.

## Japanese Quick Rules

Use the same conservative taxonomy as `humanize-japanese/references/quick-rules.md`:

- `cross_language_humanize_controls`: repeated phrases, over-complex clauses,
  generic transitions, over-explained bullets, and uniform rhythm.
- `register_monotony`: repeated sentence-final forms or modal softeners while
  preserving the intended register.
- `translationese_posteditese`: mechanical ability frames, overt pronouns,
  source-order connectives, and safe cue / review-only cue distinctions.
- `readability_texture`: sentence and clause length, kanji/kana/katakana
  balance, punctuation, and long noun chains.
- `honorific_politeness_safety`: `尊敬語`, `謙譲語I`, `謙譲語II`, `丁寧語`,
  and role-safe politeness.
- `genre_preset`: official, public help, technical, business email, product UI,
  essay/blog, creative, and opt-in `easy_japanese`.
- `stylometric_diagnostics`: function words, 助詞, POS n-grams, phrase
  patterns, and comma/読点 distribution as descriptive diagnostics only.

## Response

Return:

1. short status
2. categories addressed
3. representative before/after examples
4. self-check result

This project is a Japanese adaptation of `epoko77-ai/im-not-ai`; the Korean upstream material is retained only under `legacy/upstream-korean/`.
