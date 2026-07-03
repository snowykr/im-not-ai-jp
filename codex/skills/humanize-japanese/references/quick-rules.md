# Humanize Japanese Quick Rules

Shared rules for Japanese style rewriting. Use these as local editing
controls only: each match is a rewrite cue, not authorship proof. Preserve facts,
names, numbers, dates, citations, quotes, terminology, genre, and the intended
register unless the user explicitly asks to change them.

## cross_language_humanize_controls

Evidence grade: Heuristic inherited at the abstract behavior level.
Claim ceiling: Use as a rewrite cue, not authorship proof; it can reduce
machine-like texture but cannot identify who wrote the text.

- Reduce repeated phrases, repeated sentence shapes, and repeated abstract nouns.
- Simplify over-complex clauses and nominalized chains when meaning survives.
- Replace generic transitions and conclusions with context-specific links or
  remove them when the paragraph already carries the relation.
- Trim over-explained bullets, duplicated setup, and mechanical summary lines.
- Vary uniform rhythm by mixing short and medium sentences, while preserving the
  original facts, claims, and genre.

## register_monotony

Evidence grade: Japanese linguistic guidance plus heuristic project rule.
Claim ceiling: Repeated endings are a rewrite cue, not authorship proof; formal
Japanese can repeat endings for legitimate genre reasons.

- Preserve the document's target register: `常体`, `敬体`, `である`, `です/ます`,
  casual prose, or an intentional mixture.
- Flag long streaks of the same sentence-final form, especially `です`, `ます`,
  `でしょう`, `と思います`, `必要があります`, `ことができます`,
  `と言えます`, and `と言えるでしょう`.
- Reduce modal softener monotony such as repeated `かもしれません`,
  `と思われます`, `重要です`, `期待されます`, and `考えられます`.
- Do not humanize by random casualization. Register shifts carry social meaning.

## translationese_posteditese

Evidence grade: Moderate evidence from Japanese translationese and MT/native
Japanese research, with phrase rules kept heuristic.
Claim ceiling: Translation-like phrasing is a rewrite cue, not authorship proof;
some genres intentionally use translated, academic, legal, or technical style.

- Replace mechanical ability constructions such as `〜することができます` with
  direct potential forms or simpler verbs when safe.
- Review overused formal frames: `〜において`, `〜を通じて`, `〜に関して`,
  `〜ということ`, `〜であるという点`, and `〜することが可能です`.
- Reduce source-order connective overuse, especially sentence-initial `また`,
  `さらに`, `しかし`, `一方で`, `そのため`, and `これにより` when they act as
  mechanical paragraph glue.
- Rework overt pronouns (`私`, `あなた`, `彼`, `彼女`, `それ`, `これ`) when
  Japanese information structure would naturally omit or reframe them.
- Check abstract or inanimate subjects used as agents, passive/causative stacks,
  and nominalization chains such as repeated `〜の〜の` or `〜における〜の`.

## readability_texture

Evidence grade: Moderate evidence from Japanese readability research and public
writing guidance.
Claim ceiling: Readability stress is a rewrite cue, not authorship proof; dense
Japanese may be correct for expert, legal, academic, or reference genres.

- Balance sentence length, paragraph length, and bullet density against the
  target genre.
- Soften dense compounds and long noun chains when a concrete verb or shorter
  phrase preserves meaning.
- Watch kanji/kana/katakana balance, loanword density, and repeated abstract
  nouns such as `活用`, `推進`, `実現`, and `向上`.
- Keep necessary product names, API names, UI labels, units, citations, and
  domain terminology unchanged unless the user asks for terminology rewriting.

## honorific_politeness_safety

Evidence grade: Strong for category definitions from official Japanese honorific
guidance; heuristic for automated rewrite triggers.
Claim ceiling: Honorific mismatch is a rewrite cue, not authorship proof; safe
rewriting requires knowing speaker, listener, customer/user, company, and third
party roles.

- Preserve or repair relation-sensitive politeness across `尊敬語`, `謙譲語I`,
  `謙譲語II`, `丁寧語`, and `美化語`.
- Avoid double honorifics, wrong actor elevation/lowering, and casual rewrites
  in customer, institutional, or business contexts.
- Keep business email and support prose polite, direct, and action-oriented
  without adding unnecessary softeners or apologies.

## genre_preset

Evidence grade: Heuristic synthesis from Japanese public writing, technical
style, readability, and register guidance.
Claim ceiling: Genre mismatch is a rewrite cue, not authorship proof; follow the
user's stated target when it conflicts with these defaults.

- `public/help`: approachable `です/ます`, easy Japanese when the audience is
  broad, shorter sentences, accessible terms, concrete actions, and fewer
  formulaic conclusions.
- `technical`: concise wording, stable terminology, notation consistency,
  API names, UI labels, units, and minimal affective softeners.
- `essay/blog`: controlled stance, varied rhythm, and fewer template headings or
  summary paragraphs.
- `business email`: identify speaker, listener, company, customer/user, and
  third-party roles before changing honorifics; keep clear requests and no casual
  tone drift.
- `creative`: preserve voice, image, dialogue, pacing, and intentional
  irregularity.

## stylometric_diagnostics

Evidence grade: Strong descriptive Japanese corpus evidence for distributional
features; no rule here is calibrated for this project.
Claim ceiling: Function words, 助詞, POS n-grams, phrase patterns, comma and
読点 distribution are descriptive diagnostics and a rewrite cue, not authorship proof.

- Treat function words, 助詞 patterns, POS bigrams/trigrams, phrase patterns,
  and comma/読点 placement as distributional signals, not single-line verdicts.
- Do not call memorable phrases, punctuation, or connector lists detector proof.
- Keep severity conservative unless a project corpus validates the pattern for
  the same genre, length, and prompt conditions.
