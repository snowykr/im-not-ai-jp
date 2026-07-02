# im-not-ai-jp — Gemini CLI Extension

Fast Path extension for reducing AI-like Japanese prose while preserving meaning.

## Commands

- `/humanize-japanese [text]`
- `/humanize [text]`
- `/humanize-redo [adjustment]`

## Principles

1. Preserve facts, claims, numbers, dates, proper nouns, citations, and direct quotes.
2. Keep the source genre and register.
3. Change only spans that match Japanese AI-writing tells.
4. Avoid making formal Japanese unnecessarily casual.
5. Do not add claims, examples, or rhetorical flourishes.

## Japanese Quick Rules

Strong signals:

- repeated generic conclusions such as `重要です`, `必要があります`, `求められます`
- mechanical capability phrasing such as `〜することができます`
- empty balanced framing with repeated `一方で`, `また`, `さらに`, `加えて`
- formulaic closings such as `〜と言えるでしょう`, `〜と考えられます`

Medium signals:

- overuse of `〜において`, `〜を通じて`, `〜に関して`
- nominalized chains with `こと`, `もの`, `点`
- every sentence ending with the same polite form
- headings or bullets that explain obvious structure instead of content

Weak signals:

- unnecessary emphasis markers or quotes
- repeated abstract nouns such as `活用`, `推進`, `実現`, `向上`
- overly uniform sentence length and rhythm

## Response

Return:

1. short status
2. categories addressed
3. representative before/after examples
4. self-check result

This project is a Japanese adaptation of `epoko77-ai/im-not-ai`; the Korean upstream material is retained only under `legacy/upstream-korean/`.
