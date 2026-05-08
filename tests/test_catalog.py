from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "design-patterns"
sys.path.insert(0, str(PLUGIN / "lib"))

from pattern_catalog import load_language_profiles, load_patterns, load_playbooks, load_smells


class CatalogTests(unittest.TestCase):
    def test_patterns_include_decision_metadata(self) -> None:
        patterns = {pattern["slug"]: pattern for pattern in load_patterns()}
        strategy = patterns["strategy"]
        self.assertIn("maintainability", strategy["qualityAttributes"])
        self.assertIn("forces", strategy)
        self.assertTrue(strategy["tradeoffNotes"])
        self.assertIn("alternative", strategy["relationshipTypes"])

    def test_playbooks_and_smells_are_loaded(self) -> None:
        playbooks = {playbook["slug"]: playbook for playbook in load_playbooks()}
        smells = {smell["slug"]: smell for smell in load_smells()}
        self.assertIn("event-fanout", playbooks)
        self.assertIn("naive-exactly-once", smells)
        self.assertIn("idempotent-receiver", playbooks["event-fanout"]["patterns"])
        self.assertIn("idempotent-receiver", smells["naive-exactly-once"]["patterns"])

    def test_language_profiles_include_guidance(self) -> None:
        languages = load_language_profiles()
        self.assertIn("MassTransit", languages["csharp"]["integrationStacks"])
        self.assertTrue(languages["typescript"]["implementationNotes"])
        self.assertTrue(languages["go"]["operationalGuidance"])

    def test_cli_search_uses_full_pattern_fields(self) -> None:
        result = subprocess.run(
            [str(PLUGIN / "bin" / "patterns"), "search", "duplicate", "--scope", "integration-design", "--json"],
            cwd=ROOT,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
        )
        payload = json.loads(result.stdout)
        self.assertIn("idempotent-receiver", {item["slug"] for item in payload})

    def test_cli_recommend_and_compare(self) -> None:
        recommend = subprocess.run(
            [str(PLUGIN / "bin" / "patterns"), "recommend", "duplicate delivery repeated side effects", "--json"],
            cwd=ROOT,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
        )
        recommendations = json.loads(recommend.stdout)
        self.assertTrue(recommendations)
        self.assertIn("score", recommendations[0])

        compare = subprocess.run(
            [str(PLUGIN / "bin" / "patterns"), "compare", "strategy", "state", "--json"],
            cwd=ROOT,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
        )
        compared = json.loads(compare.stdout)
        self.assertEqual(["strategy", "state"], [item["slug"] for item in compared])


if __name__ == "__main__":
    unittest.main()
