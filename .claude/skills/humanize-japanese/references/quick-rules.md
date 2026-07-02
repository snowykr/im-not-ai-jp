# Humanize Japanese Quick Rules

This compact rule set is for the initial Fast Path. It should be expanded with real Japanese examples and corpus-backed evaluation.

## S1: Strong AI-Like Signals

| ID | Pattern | Rewrite Direction |
| --- | --- | --- |
| JA-S1-01 | Repeated generic conclusions: `重要です`, `必要があります`, `求められます` | Replace with the concrete action, condition, or consequence. |
| JA-S1-02 | Mechanical capability phrasing: `〜することができます` | Prefer direct verbs: `〜できます`, `〜します`, or a concrete active phrase. |
| JA-S1-03 | Empty balanced framing: `一方で`, `また`, `さらに`, `加えて` repeated without contrast | Keep only real logical transitions. |
| JA-S1-04 | Formulaic closing: `〜と言えるでしょう`, `〜と考えられます` | Use a direct claim when evidence supports it, or remove if redundant. |

## S2: Translation-Like Or Templated Japanese

| ID | Pattern | Rewrite Direction |
| --- | --- | --- |
| JA-S2-01 | `〜において`, `〜を通じて`, `〜に関して` overuse | Use simpler particles or restructure the sentence. |
| JA-S2-02 | Nominalized chains with `こと`, `もの`, `点` | Turn into verbs or shorter clauses. |
| JA-S2-03 | Uniform polite endings in every sentence | Vary rhythm while preserving the requested register. |
| JA-S2-04 | Over-explained headings and bullets | Merge obvious bullets or make each item carry specific information. |

## S3: Weak Signals

| ID | Pattern | Rewrite Direction |
| --- | --- | --- |
| JA-S3-01 | Excessive emphasis markers or quotes | Remove emphasis unless it marks a real term. |
| JA-S3-02 | Repeated abstract nouns such as `活用`, `推進`, `実現`, `向上` | Replace with concrete verbs or outcomes. |
| JA-S3-03 | Sentence length and rhythm too uniform | Split or combine sentences based on meaning. |

## Do Not Touch

- numbers, dates, names, laws, citations, and direct quotes
- intentionally formal public notices
- domain terms that are standard in the target field
- user-provided style constraints

## Self-Check

1. Meaning preserved.
2. No names, numbers, dates, or quotes changed.
3. Register preserved.
4. No new claims added.
5. AI-like formulas reduced.
6. The output still sounds like Japanese for the original genre, not a generic rewrite.
