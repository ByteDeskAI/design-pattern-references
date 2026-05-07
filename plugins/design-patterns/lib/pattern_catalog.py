"""Markdown-backed pattern catalog helpers."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = PLUGIN_ROOT / "data"


def _parse_frontmatter(text: str, path: Path) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing frontmatter")
    try:
        _, raw_meta, body = text.split("---", 2)
    except ValueError as exc:
        raise ValueError(f"{path}: malformed frontmatter") from exc

    meta: dict[str, Any] = {}
    current_list: str | None = None
    for raw_line in raw_meta.splitlines():
        if not raw_line.strip():
            continue
        if raw_line.startswith("  - "):
            if current_list is None:
                raise ValueError(f"{path}: list item without list key")
            meta[current_list].append(raw_line[4:].strip())
            continue
        if ":" not in raw_line:
            raise ValueError(f"{path}: malformed frontmatter line {raw_line!r}")
        key, value = raw_line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not value:
            meta[key] = []
            current_list = key
        else:
            meta[key] = value
            current_list = None
    return meta, body.strip()


def _section(body: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.MULTILINE)
    match = pattern.search(body)
    if not match:
        return ""
    next_match = re.search(r"^## .+$", body[match.end() :], re.MULTILINE)
    end = match.end() + next_match.start() if next_match else len(body)
    return body[match.end() : end].strip()


def _bullets(section: str) -> list[str]:
    return [line[2:].strip() for line in section.splitlines() if line.startswith("- ")]


def _language_notes(section: str) -> dict[str, str]:
    notes: dict[str, str] = {}
    matches = list(re.finditer(r"^### (.+?)\s*$", section, re.MULTILINE))
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        notes[match.group(1).strip()] = section[start:end].strip()
    return notes


def _load_markdown(path: Path) -> tuple[dict[str, Any], str]:
    return _parse_frontmatter(path.read_text(encoding="utf-8"), path)


def load_patterns(data_root: Path = DATA_ROOT) -> list[dict[str, Any]]:
    patterns: list[dict[str, Any]] = []
    for path in sorted((data_root / "patterns").glob("*.md")):
        meta, body = _load_markdown(path)
        pattern = dict(meta)
        pattern["intent"] = _section(body, "Intent")
        pattern["whenToUse"] = _bullets(_section(body, "When To Use"))
        pattern["avoidWhen"] = _bullets(_section(body, "Avoid When"))
        pattern["languageNotes"] = _language_notes(_section(body, "Language Notes"))
        pattern["path"] = str(path.relative_to(data_root.parent))
        patterns.append(pattern)
    return patterns


def load_language_profiles(data_root: Path = DATA_ROOT) -> dict[str, dict[str, Any]]:
    languages: dict[str, dict[str, Any]] = {}
    for path in sorted((data_root / "languages").glob("*.md")):
        meta, body = _load_markdown(path)
        slug = meta["slug"]
        languages[slug] = {
            **meta,
            "objectDesignIdioms": _bullets(_section(body, "Object Design Idioms")),
            "integrationStacks": _bullets(_section(body, "Integration Stacks")),
            "path": str(path.relative_to(data_root.parent)),
        }
    return languages


def scope_names(patterns: list[dict[str, Any]]) -> set[str]:
    groups = {group for pattern in patterns for group in pattern.get("groups", [])}
    domains = {pattern["domain"] for pattern in patterns}
    return {"all"} | groups | domains


def matches_scope(pattern: dict[str, Any], scope: str) -> bool:
    return scope == "all" or scope == pattern.get("domain") or scope in pattern.get("groups", [])


def attach_language(
    pattern: dict[str, Any],
    language: str | None,
    language_profiles: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    if not language:
        return pattern
    if language not in language_profiles:
        raise ValueError(f"Unknown language: {language}")
    if language not in pattern.get("languages", []):
        raise ValueError(f"{pattern['slug']} is not tagged for language: {language}")
    enriched = dict(pattern)
    enriched["selectedLanguage"] = language
    enriched["languageProfile"] = language_profiles[language]
    note = pattern.get("languageNotes", {}).get(language)
    if note:
        enriched["languageNote"] = note
    return enriched

