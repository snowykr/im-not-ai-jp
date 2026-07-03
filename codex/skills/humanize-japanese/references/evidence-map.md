# Humanize Japanese Evidence Map

This map explains why the shipped rules are local rewrite controls, not
authorship proof. No authorship-proof or detector marketing claims are supported.
No model-specific Japanese rewrite rules are shipped.

## cross_language_humanize_controls

- Source basis: inherited project heuristics for reducing repetition, generic
  transitions, over-complex clauses, and uniform rhythm.
- Claim limit: behavior-level editing only. These controls are not Japanese
  AI-authorship evidence without a matching project corpus.

## register_monotony

- Source basis: Bunka Agency public-writing guidance says register should match
  document purpose and audience, and that one document should keep either plain
  or polite style consistently when the genre requires it.
- Claim limit: repeated endings are a rewrite cue, not authorship proof. Formal
  Japanese may legitimately repeat endings.

## translationese_posteditese

- Source basis: Meldrum found useful evidence for third-person pronouns and
  long paragraph segmentation in contemporary Japanese translationese, while
  several expected features were weaker or genre-dependent.
- Safe cue: overt pronouns, transparent calques, and mechanical ability frames
  can be locally reviewed when the edit preserves reference and actor roles.
- Review-only cue: inanimate subjects, passive/causative stacks, connective
  order, nominalization, and loanword density need genre or corpus validation.

## readability_texture

- Source basis: Bunka Agency guidance supports reducing redundant wording,
  clarifying ambiguous ranges, handling loanwords by audience, and making public
  documents easier to read. jReadability research uses sentence length, word
  classes, and particles as readability predictors.
- Claim limit: readability stress is not an AI detector. Dense Japanese can be
  correct in legal, technical, academic, or reference genres.

## honorific_politeness_safety

- Source basis: Bunka Agency honorific guidance distinguishes relation-sensitive
  categories such as respectful, humble, polite, and beautifying language.
- Claim limit: honorific mismatch is a rewrite cue only after speaker, listener,
  company/customer, and third-party roles are known.

## genre_preset

- Source basis: Bunka Agency public-writing guidance classifies public document
  purposes and supports audience-aware wording. Immigration Services Agency and
  Bunka Agency easy Japanese guidance supports broad-audience resident-facing
  simplification when selected as an opt-in profile.
- Claim limit: genre labels are routing labels for style. They are not evidence
  that text is machine-written or model-specific.

## stylometric_diagnostics

- Source basis: PLOS ONE 2025 Japanese LLM stylometry reports value in function
  word unigrams, POS bigrams, and phrase patterns; related work also treats
  punctuation and particles as distributional features.
- Claim limit: these are descriptive diagnostics unless calibrated on this
  project corpus for the same genre, length, model, and prompt conditions.

## Source anchors

- Bunka Agency, `公用文作成の考え方`: https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/93657201.html
- Bunka Agency PDF, public-writing details: https://www.bunka.go.jp/seisaku/bunkashingikai/kokugo/hokoku/pdf/93651301_01.pdf
- Immigration Services Agency / Bunka Agency, easy Japanese guideline: https://www.moj.go.jp/isa/content/930006072.pdf
- jReadability / Hasebe-Lee: https://jreadability.net/file/hasebe-lee-2015-castelj.pdf
- PLOS ONE 2025, Japanese LLM stylometry: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335369
- Meldrum, contemporary Japanese translationese: https://honyakukenkyu.sakura.ne.jp/shotai_vol3/08_vol3_Meldrum.pdf
