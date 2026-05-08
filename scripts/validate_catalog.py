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

from pattern_catalog import load_language_profiles, load_patterns, load_playbooks, load_smells, scope_names


KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MIN_PATTERN_COUNT = 88
MIN_OBJECT_DESIGN_COUNT = 23
MIN_INTEGRATION_DESIGN_COUNT = 65
MIN_PLAYBOOK_COUNT = 8
MIN_SMELL_COUNT = 10
EXPECTED_LANGUAGES = {"csharp", "java", "typescript", "python", "go", "rust", "cpp"}
EXPECTED_SKILLS = {
    "architecture-decision",
    "architecture-issue-scan",
    "integration-flow-review",
    "pattern-advisor",
    "pattern-application",
    "pattern-finder",
}
REQUIRED_SKILL_REFERENCE_FILES = {
    "usages.md",
    "examples.md",
    "implementation.md",
    "catalog.md",
}
OBJECT_DESIGN_REFERENCE_SKILLS = {
    "architecture-decision",
    "pattern-advisor",
    "pattern-finder",
    "pattern-application",
    "architecture-issue-scan",
}
INTEGRATION_DESIGN_REFERENCE_SKILLS = OBJECT_DESIGN_REFERENCE_SKILLS | {
    "integration-flow-review",
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
    require((PLUGIN / "data" / "playbooks").is_dir(), "Missing data/playbooks Markdown directory")
    require((PLUGIN / "data" / "smells").is_dir(), "Missing data/smells Markdown directory")


def validate_references(references: list[str], valid_reference_paths: set[str], label: str) -> None:
    require(references, f"{label}: missing references frontmatter")
    require(isinstance(references, list), f"{label}: references must be a list")
    for reference in references:
        require(reference in valid_reference_paths, f"{label}: reference does not exist: {reference}")


def validate_patterns() -> None:
    patterns = load_patterns()
    valid_reference_paths = {
        str(path.relative_to(PLUGIN))
        for skill in EXPECTED_SKILLS
        for path in (PLUGIN / "skills" / skill / "references").glob("*.md")
    }
    require(len(patterns) >= MIN_PATTERN_COUNT, f"Expected at least {MIN_PATTERN_COUNT} patterns, found {len(patterns)}")
    object_count = 0
    integration_count = 0
    seen = set()
    pattern_slugs = {pattern["slug"] for pattern in patterns}
    required_pattern_fields = {
        "qualityAttributes",
        "implementationComplexity",
        "operationalRisk",
        "tradeoffs",
        "failureModes",
        "testingFocus",
        "observabilityFocus",
    }
    required_pattern_sections = {
        "forces",
        "tradeoffNotes",
        "failureModeNotes",
        "testing",
        "observability",
        "implementationNotes",
    }
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
        require(set(pattern["languages"]) <= EXPECTED_LANGUAGES, f"{slug}: unknown language tag")
        require(pattern.get("intent"), f"{slug}: missing Intent section")
        require(pattern.get("whenToUse"), f"{slug}: missing When To Use bullets")
        require(pattern.get("avoidWhen"), f"{slug}: missing Avoid When bullets")
        for field in required_pattern_fields:
            require(pattern.get(field), f"{slug}: missing {field} frontmatter")
        for field in required_pattern_sections:
            require(pattern.get(field), f"{slug}: missing {field} section")
        references = pattern.get("references", [])
        validate_references(references, valid_reference_paths, slug)
        for related in pattern.get("related", []):
            require(related in pattern_slugs, f"{slug}: related target does not exist: {related}")
        relationships = pattern.get("relationships", [])
        require(relationships, f"{slug}: missing typed relationships")
        for relationship in relationships:
            require(":" in relationship, f"{slug}: relationship must use type:slug format")
            relation_type, target = relationship.split(":", 1)
            require(KEBAB.match(relation_type) is not None, f"{slug}: invalid relationship type {relation_type}")
            require(target in pattern_slugs, f"{slug}: relationship target does not exist: {target}")
        if "object-design" in pattern["groups"]:
            object_count += 1
            require(set(pattern.get("languageNotes", {})) == set(pattern["languages"]), f"{slug}: missing language notes")
            reference_skills = {reference.split("/", 2)[1] for reference in references}
            missing = OBJECT_DESIGN_REFERENCE_SKILLS - reference_skills
            require(not missing, f"{slug}: missing object-design reference skills {sorted(missing)}")
        if "integration-design" in pattern["groups"]:
            integration_count += 1
            reference_skills = {reference.split("/", 2)[1] for reference in references}
            missing = INTEGRATION_DESIGN_REFERENCE_SKILLS - reference_skills
            require(not missing, f"{slug}: missing integration-design reference skills {sorted(missing)}")
        require(KEBAB.match(pattern["domain"]) is not None, f"{slug}: invalid domain")
        for group in pattern["groups"]:
            require(KEBAB.match(group) is not None, f"{slug}: invalid group {group}")
    require(object_count >= MIN_OBJECT_DESIGN_COUNT, f"Expected at least {MIN_OBJECT_DESIGN_COUNT} object-design patterns, found {object_count}")
    require(integration_count >= MIN_INTEGRATION_DESIGN_COUNT, f"Expected at least {MIN_INTEGRATION_DESIGN_COUNT} integration-design patterns, found {integration_count}")
    require({"all", "object-design", "integration-design"} <= scope_names(patterns), "Missing core query scopes")


def validate_playbooks_and_smells() -> None:
    patterns = load_patterns()
    playbooks = load_playbooks()
    smells = load_smells()
    pattern_slugs = {pattern["slug"] for pattern in patterns}
    smell_slugs = {smell["slug"] for smell in smells}
    valid_reference_paths = {
        str(path.relative_to(PLUGIN))
        for skill in EXPECTED_SKILLS
        for path in (PLUGIN / "skills" / skill / "references").glob("*.md")
    }
    require(len(playbooks) >= MIN_PLAYBOOK_COUNT, f"Expected at least {MIN_PLAYBOOK_COUNT} playbooks, found {len(playbooks)}")
    require(len(smells) >= MIN_SMELL_COUNT, f"Expected at least {MIN_SMELL_COUNT} smells, found {len(smells)}")
    seen = set()
    for playbook in playbooks:
        slug = playbook["slug"]
        require(KEBAB.match(slug) is not None, f"Invalid playbook slug {slug}")
        require(slug not in seen, f"Duplicate playbook slug {slug}")
        seen.add(slug)
        require("architecture-playbook" in playbook.get("groups", []), f"{slug}: missing architecture-playbook group")
        require(playbook.get("patterns"), f"{slug}: missing playbook patterns")
        for pattern in playbook.get("patterns", []):
            require(pattern in pattern_slugs, f"{slug}: playbook pattern target does not exist: {pattern}")
        for smell in playbook.get("smells", []):
            require(smell in smell_slugs, f"{slug}: playbook smell target does not exist: {smell}")
        for section in ("intent", "whenToUse", "avoidWhen", "patternSet", "implementationSteps", "verification"):
            require(playbook.get(section), f"{slug}: missing {section} section")
        validate_references(playbook.get("references", []), valid_reference_paths, slug)
    seen.clear()
    for smell in smells:
        slug = smell["slug"]
        require(KEBAB.match(slug) is not None, f"Invalid smell slug {slug}")
        require(slug not in seen, f"Duplicate smell slug {slug}")
        seen.add(slug)
        require("architecture-smell" in smell.get("groups", []), f"{slug}: missing architecture-smell group")
        require(smell.get("patterns"), f"{slug}: missing smell pattern responses")
        for pattern in smell.get("patterns", []):
            require(pattern in pattern_slugs, f"{slug}: smell pattern target does not exist: {pattern}")
        for section in ("symptom", "whyItMatters", "patternResponses", "falsePositives", "checks"):
            require(smell.get(section), f"{slug}: missing {section} section")
        validate_references(smell.get("references", []), valid_reference_paths, slug)


def validate_languages() -> None:
    languages = load_language_profiles()
    require(set(languages) == EXPECTED_LANGUAGES, "Language Markdown catalog does not match expected language set")
    for slug, language in languages.items():
        require(language.get("displayName"), f"{slug}: missing displayName")
        require(language.get("objectDesignIdioms"), f"{slug}: missing Object Design Idioms")
        require(language.get("integrationStacks"), f"{slug}: missing Integration Stacks")
        require(language.get("implementationNotes"), f"{slug}: missing Implementation Notes")
        require(language.get("testingGuidance"), f"{slug}: missing Testing Guidance")
        require(language.get("operationalGuidance"), f"{slug}: missing Operational Guidance")


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
        references_root = skills_root / skill / "references"
        require(references_root.is_dir(), f"{skill}: missing references directory")
        reference_files = {path.name for path in references_root.glob("*.md")}
        missing_references = REQUIRED_SKILL_REFERENCE_FILES - reference_files
        require(not missing_references, f"{skill}: missing reference files {sorted(missing_references)}")
        for reference_file in REQUIRED_SKILL_REFERENCE_FILES:
            reference_path = references_root / reference_file
            reference_text = reference_path.read_text(encoding="utf-8")
            require(f"(references/{reference_file})" in text, f"{skill}: SKILL.md must link references/{reference_file}")
            require(len(reference_text.split()) >= 80, f"{skill}: references/{reference_file} must contain substantive guidance")
        usages = (references_root / "usages.md").read_text(encoding="utf-8")
        require("## Output Contract" in usages, f"{skill}: usages.md must define an Output Contract")


def validate_evals() -> None:
    evals_path = ROOT / "evals" / "evals.json"
    require(evals_path.exists(), "Missing evals/evals.json")
    payload = load_json(evals_path)
    require(payload.get("skill_name") == "design-patterns", "evals/evals.json: skill_name must be design-patterns")
    evals = payload.get("evals", [])
    require(len(evals) >= 3, "evals/evals.json: expected at least 3 evals")
    seen = set()
    for item in evals:
        eval_id = item.get("id")
        require(eval_id not in seen, f"evals/evals.json: duplicate eval id {eval_id}")
        seen.add(eval_id)
        require(item.get("prompt"), f"evals/evals.json: eval {eval_id} missing prompt")
        require(item.get("expected_output"), f"evals/evals.json: eval {eval_id} missing expected_output")
        require(isinstance(item.get("files", []), list), f"evals/evals.json: eval {eval_id} files must be a list")


def main() -> int:
    validate_claude_manifest()
    validate_codex_manifest()
    validate_markdown_only_data()
    validate_patterns()
    validate_playbooks_and_smells()
    validate_languages()
    validate_skills()
    validate_evals()
    print("Marketplace metadata, Markdown catalog, playbooks, smells, evals, and skill metadata validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
