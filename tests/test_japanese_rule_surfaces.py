from __future__ import annotations

from pathlib import Path
import unittest


_REPO_ROOT = Path(__file__).resolve().parents[1]
_CODEX_QUICK_RULES_PATH = (
    _REPO_ROOT / "codex/skills/humanize-japanese/references/quick-rules.md"
)
_CLAUDE_QUICK_RULES_PATH = (
    _REPO_ROOT / ".claude/skills/humanize-japanese/references/quick-rules.md"
)
_CODEX_EVIDENCE_MAP_PATH = (
    _REPO_ROOT / "codex/skills/humanize-japanese/references/evidence-map.md"
)
_CLAUDE_EVIDENCE_MAP_PATH = (
    _REPO_ROOT / ".claude/skills/humanize-japanese/references/evidence-map.md"
)
_ENTRYPOINT_PATHS = (
    _REPO_ROOT / "codex/skills/humanize-japanese/SKILL.md",
    _REPO_ROOT / ".claude/skills/humanize-japanese/SKILL.md",
    _REPO_ROOT / "GEMINI.md",
    _REPO_ROOT / "commands/humanize-japanese.toml",
    _REPO_ROOT / "commands/humanize.toml",
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
_EVIDENCE_SOURCE_MARKERS = (
    "Bunka Agency",
    "Immigration Services Agency",
    "jReadability",
    "PLOS ONE 2025",
    "Meldrum",
)
_TRANSLATIONESE_CUE_STRENGTH_MARKERS = (
    "safe cue",
    "review-only cue",
    "Do not blanket-rewrite passive, causative, nominalization, or inanimate subjects.",
)
_ENTRYPOINT_TAXONOMY_MARKERS = (
    "register_monotony",
    "translationese_posteditese",
    "readability_texture",
    "honorific_politeness_safety",
    "genre_preset",
    "stylometric_diagnostics",
    "rewrite cue, not authorship proof",
)
_DETECTOR_DRIFT_MARKERS = (
    "S1/S2/S3",
    "AI-writing tells",
    "AI文体シグナル",
    "Strong signals:",
    "Medium signals:",
    "Weak signals:",
)


def _assert_phrases(text: str, phrases: tuple[str, ...], label: str) -> None:
    missing = [phrase for phrase in phrases if phrase not in text]
    if missing:
        raise AssertionError(f"{label} missing shipped rule phrases: {missing}")


def _rule_section(rule_text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = rule_text.find(marker)
    if start == -1:
        raise AssertionError(f"missing shipped Japanese rule heading: {heading}")
    next_start = rule_text.find("\n## ", start + len(marker))
    if next_start == -1:
        return rule_text[start:]
    return rule_text[start:next_start]


def _assert_evidence_map(evidence_text: str) -> None:
    for heading in _RULE_HEADINGS:
        _assert_phrases(evidence_text, (f"## {heading}",), "evidence-map-headings")
    _assert_phrases(
        evidence_text,
        _EVIDENCE_SOURCE_MARKERS,
        "evidence-map-source-anchors",
    )
    _assert_phrases(
        evidence_text,
        (
            "No model-specific Japanese rewrite rules are shipped.",
            "No authorship-proof or detector marketing claims are supported.",
        ),
        "evidence-map-claim-ceiling",
    )


def _assert_entrypoint_uses_current_taxonomy(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    _assert_phrases(text, _ENTRYPOINT_TAXONOMY_MARKERS, str(path))
    stale = [marker for marker in _DETECTOR_DRIFT_MARKERS if marker in text]
    if stale:
        raise AssertionError(f"{path} contains stale detector framing: {stale}")


class TestJapaneseRuleSurfaces(unittest.TestCase):
    def test_shipped_quick_rules_link_to_evidence_map(self) -> None:
        rule_text = _CODEX_QUICK_RULES_PATH.read_text(encoding="utf-8")
        evidence_text = _CODEX_EVIDENCE_MAP_PATH.read_text(encoding="utf-8")

        _assert_phrases(
            rule_text,
            (
                "evidence-map.md",
                "`easy_japanese`",
                "opt-in profile",
            ),
            "quick-rules-evidence-map-link",
        )
        _assert_phrases(
            _rule_section(rule_text, "translationese_posteditese"),
            _TRANSLATIONESE_CUE_STRENGTH_MARKERS,
            "translationese-cue-strength",
        )
        _assert_evidence_map(evidence_text)

    def test_claude_and_codex_evidence_maps_stay_in_sync(self) -> None:
        claude_rules = _CLAUDE_QUICK_RULES_PATH.read_text(encoding="utf-8")
        codex_rules = _CODEX_QUICK_RULES_PATH.read_text(encoding="utf-8")
        claude_evidence = _CLAUDE_EVIDENCE_MAP_PATH.read_text(encoding="utf-8")
        codex_evidence = _CODEX_EVIDENCE_MAP_PATH.read_text(encoding="utf-8")

        self.assertEqual(codex_rules, claude_rules)
        self.assertEqual(codex_evidence, claude_evidence)

    def test_entrypoints_use_current_japanese_taxonomy(self) -> None:
        for path in _ENTRYPOINT_PATHS:
            with self.subTest(path=path):
                _assert_entrypoint_uses_current_taxonomy(path)


if __name__ == "__main__":
    _ = unittest.main()
