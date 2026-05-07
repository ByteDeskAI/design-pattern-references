#!/usr/bin/env python3
"""Validate marketplace manifests and Markdown pattern catalog completeness."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "design-patterns"
sys.path.insert(0, str(PLUGIN / "lib"))

from pattern_catalog import load_language_profiles, load_patterns, scope_names


KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EXPECTED_PATTERN_COUNT = 88
EXPECTED_OBJECT_DESIGN_COUNT = 23
EXPECTED_INTEGRATION_DESIGN_COUNT = 65
EXPECTED_LANGUAGES = {"csharp", "java", "typescript", "python", "go", "rust", "cpp"}
EXPECTED_SKILLS = {
    "architecture-issue-scan",
    "integration-flow-review",
    "pattern-advisor",
    "pattern-application",
    "pattern-finder",
}
REQUIRED_SKILL_FRONTMATTER = {
    "name",
    "description",
    "when_to_use",
    "argument-hint",
    "user-invocable",
    "disable-model-invocation",
    "allowed-tools",
    "model",
}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def parse_frontmatter(text: str, label: str) -> dict[str, str]:
    require(text.startswith("---\n"), f"{label}: missing YAML frontmatter")
    parts = text.split("---", 2)
    require(len(parts) == 3, f"{label}: malformed YAML frontmatter")
    frontmatter: dict[str, str] = {}
    for line in parts[1].splitlines():
        if not line.strip():
            continue
        require(":" in line, f"{label}: malformed frontmatter line {line!r}")
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip('"')
    return frontmatter


def validate_claude_manifest() -> None:
    marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json")
    plugin = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
    require(KEBAB.match(marketplace["name"]) is not None, "Claude marketplace name must be kebab-case")
    require(KEBAB.match(plugin["name"]) is not None, "Claude plugin name must be kebab-case")
    require(marketplace["plugins"][0]["source"] == "./plugins/design-patterns", "Claude marketplace source must stay relative to marketplace root")
    require(marketplace["plugins"][0]["name"] == plugin["name"], "Claude marketplace plugin name must match plugin manifest")
    require(marketplace["plugins"][0]["version"] == plugin["version"], "Claude marketplace and plugin versions must match")


def validate_codex_manifest() -> None:
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    require(KEBAB.match(marketplace["name"]) is not None, "Codex marketplace name must be kebab-case")
    require(KEBAB.match(plugin["name"]) is not None, "Codex plugin name must be kebab-case")
    require(marketplace["plugins"], "Codex marketplace must list at least one plugin")
    entry = marketplace["plugins"][0]
    require(entry["name"] == plugin["name"], "Codex marketplace plugin name must match plugin manifest")
    require(entry["source"]["source"] == "local", "Codex marketplace source must be local")
    require(entry["source"]["path"] == "./plugins/design-patterns", "Codex marketplace source path must stay relative to marketplace root")
    require(entry["policy"]["installation"] in {"NOT_AVAILABLE", "AVAILABLE", "INSTALLED_BY_DEFAULT"}, "Codex installation policy is invalid")
    require(entry["policy"]["authentication"] in {"ON_INSTALL", "ON_USE"}, "Codex authentication policy is invalid")
    require(entry.get("category"), "Codex marketplace entry must include category")
    require(plugin["skills"] == "./skills/", "Codex plugin must expose the shared skills directory")
    require(plugin["version"] == load_json(PLUGIN / ".claude-plugin" / "plugin.json")["version"], "Claude and Codex plugin versions must match")


def validate_markdown_only_data() -> None:
    data_files = list((PLUGIN / "data").rglob("*"))
    json_files = [path for path in data_files if path.suffix == ".json"]
    require(not json_files, "Pattern data must be stored as Markdown, not JSON")
    require((PLUGIN / "data" / "patterns").is_dir(), "Missing data/patterns Markdown directory")
    require((PLUGIN / "data" / "languages").is_dir(), "Missing data/languages Markdown directory")


def validate_patterns() -> None:
    patterns = load_patterns()
    require(len(patterns) == EXPECTED_PATTERN_COUNT, f"Expected {EXPECTED_PATTERN_COUNT} patterns, found {len(patterns)}")
    object_count = 0
    integration_count = 0
    seen = set()
    for pattern in patterns:
        slug = pattern["slug"]
        require(KEBAB.match(slug) is not None, f"Invalid slug {slug}")
        require(slug not in seen, f"Duplicate slug {slug}")
        seen.add(slug)
        require(pattern.get("name"), f"{slug}: missing name")
        require(pattern.get("domain"), f"{slug}: missing domain")
        require(pattern.get("category"), f"{slug}: missing category")
        require(pattern.get("groups"), f"{slug}: missing groups")
        require(pattern.get("languages"), f"{slug}: missing languages")
        require(set(pattern["languages"]) == EXPECTED_LANGUAGES, f"{slug}: incomplete language tags")
        require(pattern.get("intent"), f"{slug}: missing Intent section")
        require(pattern.get("whenToUse"), f"{slug}: missing When To Use bullets")
        require(pattern.get("avoidWhen"), f"{slug}: missing Avoid When bullets")
        if "object-design" in pattern["groups"]:
            object_count += 1
            require(set(pattern.get("languageNotes", {})) == EXPECTED_LANGUAGES, f"{slug}: missing language notes")
        if "integration-design" in pattern["groups"]:
            integration_count += 1
        require(KEBAB.match(pattern["domain"]) is not None, f"{slug}: invalid domain")
        for group in pattern["groups"]:
            require(KEBAB.match(group) is not None, f"{slug}: invalid group {group}")
    require(object_count == EXPECTED_OBJECT_DESIGN_COUNT, f"Expected {EXPECTED_OBJECT_DESIGN_COUNT} object-design patterns, found {object_count}")
    require(integration_count == EXPECTED_INTEGRATION_DESIGN_COUNT, f"Expected {EXPECTED_INTEGRATION_DESIGN_COUNT} integration-design patterns, found {integration_count}")
    require({"all", "object-design", "integration-design"} <= scope_names(patterns), "Missing core query scopes")


def validate_languages() -> None:
    languages = load_language_profiles()
    require(set(languages) == EXPECTED_LANGUAGES, "Language Markdown catalog does not match expected language set")
    for slug, language in languages.items():
        require(language.get("displayName"), f"{slug}: missing displayName")
        require(language.get("objectDesignIdioms"), f"{slug}: missing Object Design Idioms")
        require(language.get("integrationStacks"), f"{slug}: missing Integration Stacks")


def validate_skills() -> None:
    skills_root = PLUGIN / "skills"
    skill_names = {path.name for path in skills_root.iterdir() if path.is_dir()}
    require(EXPECTED_SKILLS <= skill_names, "Plugin is missing required skills")
    for skill in EXPECTED_SKILLS:
        skill_file = skills_root / skill / "SKILL.md"
        require(skill_file.exists(), f"{skill}: missing SKILL.md")
        text = skill_file.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text, skill)
        missing = REQUIRED_SKILL_FRONTMATTER - set(frontmatter)
        require(not missing, f"{skill}: missing frontmatter fields {sorted(missing)}")
        require(frontmatter["name"] == skill, f"{skill}: name must match skill directory")
        require(frontmatter["description"], f"{skill}: description must not be empty")
        require(frontmatter["when_to_use"], f"{skill}: when_to_use must not be empty")
        require(frontmatter["argument-hint"].startswith("["), f"{skill}: argument-hint should describe slash-command arguments")
        require(frontmatter["user-invocable"] == "true", f"{skill}: user-invocable must be explicit true")
        require(frontmatter["disable-model-invocation"] == "false", f"{skill}: disable-model-invocation must be explicit false")
        require(frontmatter["model"] == "inherit", f"{skill}: model must inherit caller context")
        require("Bash(patterns *)" in frontmatter["allowed-tools"], f"{skill}: allowed-tools must include patterns lookup")


def main() -> int:
    validate_claude_manifest()
    validate_codex_manifest()
    validate_markdown_only_data()
    validate_patterns()
    validate_languages()
    validate_skills()
    print("Marketplace metadata, Markdown catalog, and skill metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
