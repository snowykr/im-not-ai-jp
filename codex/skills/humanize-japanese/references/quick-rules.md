# Humanize Japanese Quick Rules

Shared rules for Japanese style rewriting. Use these as local editing
controls only: each match is a rewrite cue, not authorship proof. Preserve facts,
names, numbers, dates, citations, quotes, terminology, genre, and the intended
register unless the user explicitly asks to change them. See `evidence-map.md`
for source anchors, claim limits, and unshipped research leads.

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
- Use these register target names when a workflow needs an explicit target:
  `plain`, `neutral`, `polite`, `formal`, `customer_service_polite`.
- Before: `本サービスを利用することができます。`
  After: `本サービスを利用できます。`
- Before: `ご確認いただけますと幸いです。ご連絡いただけますと幸いです。`
  After: `ご確認のうえ、ご連絡ください。`
- Do not rewrite: `このAPIは、認証後にのみ呼び出せます。`
  This is already direct technical prose; making it casual or adding softeners
  would change the register without improving readability.

## translationese_posteditese

Evidence grade: Moderate evidence from Japanese translationese and MT/native
Japanese research, with phrase rules kept heuristic.
Claim ceiling: Translation-like phrasing is a rewrite cue, not authorship proof;
some genres intentionally use translated, academic, legal, or technical style.

- Replace mechanical ability constructions such as `〜することができます` with
  direct potential forms or simpler verbs when safe.
- Track the cue categories as style-risk categories only: overt pronouns,
  source-order connectives, inanimate subjects, nominalization chains, and
  calque-like phrasing. They are rewrite/style-risk cues, not detector claims.
- Treat overt pronouns, transparent calques, and mechanical ability frames as a
  safe cue for local review when the surrounding sentence supports the edit.
- Treat inanimate subjects, passive/causative stacks, connective order,
  nominalization, and loanword density as a review-only cue unless the genre and
  corpus context justify a rewrite.
- Do not blanket-rewrite passive, causative, nominalization, or inanimate subjects.
- Review overused formal frames: `〜において`, `〜を通じて`, `〜に関して`,
  `〜ということ`, `〜であるという点`, and `〜することが可能です`.
- Reduce source-order connective overuse, especially sentence-initial `また`,
  `さらに`, `しかし`, `一方で`, `そのため`, and `これにより` when they act as
  mechanical paragraph glue.
- Rework overt pronouns (`私`, `あなた`, `彼`, `彼女`, `それ`, `これ`) when
  Japanese information structure would naturally omit or reframe them.
- Check abstract or inanimate subjects used as agents, passive/causative stacks,
  and nominalization chains such as repeated `〜の〜の` or `〜における〜の`.
- Before: `この変更は、利用者に新しい画面を表示させます。`
  After: `この変更により、利用者には新しい画面が表示されます。`
- Before: `あなたは設定画面において通知を変更することができます。`
  After: `設定画面で通知を変更できます。`
- Do not rewrite: `彼女は取締役として契約書に署名しました。`
  The pronoun identifies a real person in context; omitting it could obscure
  who acted.

## readability_texture

Evidence grade: Moderate evidence from Japanese readability research and public
writing guidance.
Claim ceiling: Readability stress is a rewrite cue, not authorship proof; dense
Japanese may be correct for expert, legal, academic, or reference genres.

- Balance sentence length, paragraph length, and bullet density against the
  target genre.
- Use Japanese punctuation deliberately: `、` should clarify clause boundaries,
  and `。` should close complete thoughts. Do not scatter punctuation only to
  imitate a different rhythm.
- Watch clause length, not only sentence length. Split or reorder when a reader
  must hold too many modifiers before reaching the main verb.
- Soften dense compounds and long noun chains when a concrete verb or shorter
  phrase preserves meaning.
- Watch kanji/kana/katakana balance, loanword density, and repeated abstract
  nouns such as `活用`, `推進`, `実現`, and `向上`.
- Keep kanji/kana balance natural for the audience: over-converting kanji to
  kana can look childish or vague, while dense kanji chains can slow scanning.
- Avoid over-simplification. Do not remove legally, technically, or socially
  necessary distinctions just to make a sentence shorter.
- Keep necessary product names, API names, UI labels, units, citations, and
  domain terminology unchanged unless the user asks for terminology rewriting.
- Before: `利用開始前に管理者による権限設定確認作業の実施が必要です。`
  After: `利用を開始する前に、管理者による権限設定の確認が必要です。`
- Do not rewrite: `本契約に基づく損害賠償責任は、直接かつ通常の損害に限ります。`
  This legal wording may need the dense terms and punctuation as written.

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

- `official_notice`: formal public-facing prose, stable terminology, dates and
  obligations intact, and no casual drift.
- `public_help` (legacy label `public/help`): approachable `です/ます`, easy Japanese
  when the audience is broad, shorter sentences, accessible terms, concrete
  actions, and fewer formulaic conclusions.
- `easy_japanese`: opt-in profile for public, administrative, medical,
  disaster, welfare, and resident-facing text; explain unfamiliar loanwords,
  expand acronyms on first use, keep one idea per sentence, make dates/times
  explicit, avoid double negatives, and reduce honorific density when
  comprehension matters more than ceremonial politeness.
- `technical`: concise wording, stable terminology, notation consistency,
  API names, UI labels, units, and minimal affective softeners.
- `business_email` (legacy label `business email`): identify speaker, listener,
  company, customer/user, and third-party roles before changing honorifics; keep
  clear requests and no casual tone drift.
- `product_ui`: concise labels, consistent verbs, no ornamental politeness, and
  product terms unchanged.
- `essay_blog`: controlled stance, varied rhythm, and fewer template headings or
  summary paragraphs.
- `creative`: preserve voice, image, dialogue, pacing, and intentional
  irregularity.
- Do not rewrite: genre names are routing labels for style, not evidence that a
  text is machine-written or model-specific.

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
