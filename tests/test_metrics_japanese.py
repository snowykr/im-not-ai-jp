from __future__ import annotations

from pathlib import Path
import unittest


_QUICK_RULES_PATH = Path("codex/skills/humanize-japanese/references/quick-rules.md")
_CLAUDE_QUICK_RULES_PATH = Path(
    ".claude/skills/humanize-japanese/references/quick-rules.md"
)
_CODEX_QUICK_RULES_PATH = Path(
    "codex/skills/humanize-japanese/references/quick-rules.md"
)
_RULE_HEADINGS = (
    "cross_language_humanize_controls",
    "register_monotony",
    "translationese_posteditese",
    "readability_texture",
    "honorific_politeness_safety",
    "genre_preset",
    "stylometric_diagnostics",
)
_REGISTER_TARGETS = ("plain", "neutral", "polite", "formal", "customer_service_polite")
_GENRE_PROFILES = (
    "official_notice",
    "public_help",
    "technical",
    "business_email",
    "product_ui",
    "essay_blog",
    "creative",
)
_TRANSLATIONESE_CUE_CATEGORIES = (
    "overt pronouns",
    "source-order connectives",
    "inanimate subjects",
    "nominalization chains",
    "calque-like phrasing",
)
_PUNCTUATION_READABILITY_CUES = (
    "`、`",
    "`。`",
    "clause length",
    "kanji/kana balance",
    "over-simplification",
)
_EXAMPLE_MARKERS = ("Before:", "After:", "Do not rewrite:")
_SECTION_EXAMPLES = {
    "register_monotony": (
        "本サービスを利用することができます",
        "本サービスを利用できます",
        "このAPIは、認証後にのみ呼び出せます。",
    ),
    "translationese_posteditese": (
        "この変更は、利用者に新しい画面を表示させます。",
        "設定画面で通知を変更できます。",
        "彼女は取締役として契約書に署名しました。",
    ),
    "readability_texture": (
        "利用開始前に管理者による権限設定確認作業の実施が必要です。",
        "利用を開始する前に、管理者による権限設定の確認が必要です。",
        "本契約に基づく損害賠償責任は、直接かつ通常の損害に限ります。",
    ),
}


def _quick_rules_text() -> str:
    return _QUICK_RULES_PATH.read_text(encoding="utf-8")


def _rule_section(rule_text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = rule_text.find(marker)
    if start == -1:
        raise AssertionError(f"missing shipped Japanese rule heading: {heading}")
    next_start = rule_text.find("\n## ", start + len(marker))
    if next_start == -1:
        return rule_text[start:]
    return rule_text[start:next_start]


def _assert_phrases(text: str, phrases: tuple[str, ...], label: str) -> None:
    missing = [phrase for phrase in phrases if phrase not in text]
    if missing:
        raise AssertionError(f"{label} missing shipped rule phrases: {missing}")


def _assert_shipped_quick_rules(rule_text: str) -> None:
    _assert_phrases(
        rule_text,
        (
            "local editing\ncontrols only",
            "rewrite cue, not authorship proof",
            "cannot identify who wrote the text",
        ),
        "claim-safety",
    )

    for heading in _RULE_HEADINGS:
        section = _rule_section(rule_text, heading)
        _assert_phrases(
            section,
            ("Evidence grade:", "Claim ceiling:", "rewrite cue, not authorship proof"),
            heading,
        )

    _assert_phrases(
        _rule_section(rule_text, "cross_language_humanize_controls"),
        (
            "repeated phrases",
            "over-complex clauses",
            "generic transitions",
            "over-explained bullets",
            "uniform rhythm",
        ),
        "jp-repetition-generic-connector",
    )
    _assert_phrases(
        _rule_section(rule_text, "register_monotony"),
        (
            "です/ます",
            "same sentence-final form",
            "formal\nJapanese can repeat endings for legitimate genre reasons",
            "Do not humanize by random casualization",
        ),
        "jp-register-monotony-ending-streak",
    )
    _assert_phrases(
        _rule_section(rule_text, "translationese_posteditese"),
        (
            "〜することができます",
            "〜において",
            "sentence-initial `また`",
            "nominalization chains",
        ),
        "jp-translationese-nominalization-chain",
    )
    _assert_phrases(
        _rule_section(rule_text, "readability_texture"),
        (
            "sentence length",
            "kanji/kana/katakana balance",
            "long noun chains",
            "domain terminology unchanged",
        ),
        "jp-readability-dense-sentence",
    )
    _assert_phrases(
        _rule_section(rule_text, "honorific_politeness_safety"),
        (
            "尊敬語",
            "謙譲語I",
            "customer, institutional, or business contexts",
        ),
        "honorific-politeness-safety",
    )
    _assert_phrases(
        _rule_section(rule_text, "genre_preset"),
        (
            "`public_help`",
            "legacy label `public/help`",
            "`technical`",
            "`business_email`",
            "legacy label `business email`",
            "easy Japanese",
            "API names",
            "speaker, listener",
            "no casual",
            "target",
        ),
        "formal-public-notice-guard",
    )
    _assert_phrases(
        _rule_section(rule_text, "stylometric_diagnostics"),
        (
            "no rule here is calibrated",
            "distributional signals",
            "not single-line verdicts",
        ),
        "stylometric-diagnostics",
    )


def _assert_shipped_quick_rules_include_japanese_examples(rule_text: str) -> None:
    _assert_phrases(
        _rule_section(rule_text, "register_monotony"),
        _REGISTER_TARGETS,
        "register-target-names",
    )
    _assert_phrases(
        _rule_section(rule_text, "genre_preset"),
        _GENRE_PROFILES,
        "genre-profile-names",
    )
    _assert_phrases(
        _rule_section(rule_text, "translationese_posteditese"),
        _TRANSLATIONESE_CUE_CATEGORIES,
        "translationese-cue-categories",
    )
    _assert_phrases(
        _rule_section(rule_text, "readability_texture"),
        _PUNCTUATION_READABILITY_CUES,
        "punctuation-readability-cues",
    )
    for heading, examples in _SECTION_EXAMPLES.items():
        section = _rule_section(rule_text, heading)
        _assert_phrases(
            section,
            _EXAMPLE_MARKERS,
            f"{heading}-japanese-example-labels",
        )
        _assert_phrases(section, examples, f"{heading}-concrete-japanese-examples")


class TestJapaneseQuickRules(unittest.TestCase):
    def test_shipped_quick_rules_define_japanese_rule_behavior(self) -> None:
        rule_text = _quick_rules_text()

        _assert_shipped_quick_rules(rule_text)

    def test_shipped_quick_rules_include_concrete_japanese_examples(self) -> None:
        rule_text = _quick_rules_text()

        _assert_shipped_quick_rules_include_japanese_examples(rule_text)

    def test_claude_and_codex_rules_stay_in_sync(self) -> None:
        claude_rules = _CLAUDE_QUICK_RULES_PATH.read_text(encoding="utf-8")
        codex_rules = _CODEX_QUICK_RULES_PATH.read_text(encoding="utf-8")

        self.assertEqual(codex_rules, claude_rules)

    def test_shipped_quick_rules_guard_fails_when_claim_safety_is_removed(
        self,
    ) -> None:
        rule_text = _quick_rules_text()
        mutated = (
            rule_text.replace("rewrite cue, not authorship proof", "authorship proof")
            .replace(
                "formal\nJapanese can repeat endings for legitimate genre reasons",
                "",
            )
            .replace("Do not humanize by random casualization", "")
        )

        with self.assertRaises(AssertionError):
            _assert_shipped_quick_rules(mutated)

if __name__ == "__main__":
    _ = unittest.main()
