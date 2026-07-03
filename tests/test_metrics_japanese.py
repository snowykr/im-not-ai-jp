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
            "`public/help`",
            "`technical`",
            "`business email`",
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


class TestJapaneseQuickRules(unittest.TestCase):
    def test_shipped_quick_rules_define_japanese_rule_behavior(self) -> None:
        rule_text = _quick_rules_text()

        _assert_shipped_quick_rules(rule_text)

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
    unittest.main()
