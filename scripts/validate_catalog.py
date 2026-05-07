#!/usr/bin/env python3
"""Validate marketplace manifests and pattern catalog completeness."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "design-patterns"
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_GOF_COUNT = 23
EXPECTED_EIP_COUNT = 65
EXPECTED_LANGUAGES = {"csharp", "java", "typescript", "python", "go", "rust", "cpp"}
EXPECTED_SKILLS = {
    "architecture-issue-scan",
    "integration-flow-review",
    "pattern-advisor",
    "pattern-application",
    "pattern-finder",
}


def load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def validate_manifest() -> None:
    marketplace = load(ROOT / ".claude-plugin" / "marketplace.json")
    plugin = load(PLUGIN / ".claude-plugin" / "plugin.json")
    require(KEBAB.match(marketplace["name"]) is not None, "Marketplace name must be kebab-case")
    require(KEBAB.match(plugin["name"]) is not None, "Plugin name must be kebab-case")
    require(marketplace["plugins"][0]["source"] == "./plugins/design-patterns", "Marketplace source must stay relative to marketplace root")
    require(marketplace["plugins"][0]["name"] == plugin["name"], "Marketplace plugin name must match plugin manifest")
    require(marketplace["plugins"][0]["version"] == plugin["version"], "Marketplace and plugin versions must match")


def validate_catalog(name: str, expected_count: int) -> dict:
    catalog = load(PLUGIN / "data" / name)
    patterns = catalog["patterns"]
    require(len(patterns) == expected_count, f"{name} expected {expected_count} patterns, found {len(patterns)}")
    seen = set()
    for pattern in patterns:
        slug = pattern["slug"]
        require(KEBAB.match(slug) is not None, f"{name}: invalid slug {slug}")
        require(slug not in seen, f"{name}: duplicate slug {slug}")
        seen.add(slug)
        require(pattern.get("name"), f"{name}: missing name for {slug}")
        require(pattern.get("intent"), f"{name}: missing intent for {slug}")
        require(pattern.get("whenToUse"), f"{name}: missing whenToUse for {slug}")
        require(pattern.get("avoidWhen"), f"{name}: missing avoidWhen for {slug}")
    return catalog


def validate_gof_languages(gof: dict) -> None:
    require(set(gof["languages"]) == EXPECTED_LANGUAGES, "GoF language list is incomplete")
    for pattern in gof["patterns"]:
        notes = pattern.get("languageNotes", {})
        require(set(notes) == EXPECTED_LANGUAGES, f"GoF pattern {pattern['slug']} has incomplete language notes")


def validate_language_catalog() -> None:
    languages = load(PLUGIN / "data" / "languages.json")["languages"]
    require(set(languages) == EXPECTED_LANGUAGES, "languages.json does not match expected language set")
    for slug, language in languages.items():
        require(language.get("displayName"), f"{slug}: missing displayName")
        require(language.get("gofIdioms"), f"{slug}: missing gofIdioms")
        require(language.get("eipStacks"), f"{slug}: missing eipStacks")


def validate_skills() -> None:
    skills_root = PLUGIN / "skills"
    skill_names = {path.name for path in skills_root.iterdir() if path.is_dir()}
    require(EXPECTED_SKILLS <= skill_names, "Plugin is missing required skills")
    for skill in EXPECTED_SKILLS:
        skill_file = skills_root / skill / "SKILL.md"
        require(skill_file.exists(), f"{skill}: missing SKILL.md")
        text = skill_file.read_text(encoding="utf-8")
        require(text.startswith("---\n"), f"{skill}: missing YAML frontmatter")
        require("description:" in text.split("---", 2)[1], f"{skill}: missing description frontmatter")


def main() -> int:
    validate_manifest()
    gof = validate_catalog("gof.json", EXPECTED_GOF_COUNT)
    validate_catalog("eip.json", EXPECTED_EIP_COUNT)
    validate_gof_languages(gof)
    validate_language_catalog()
    validate_skills()
    print("Catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
