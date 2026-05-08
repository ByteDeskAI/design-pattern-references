# Design Pattern References

Claude Code and Codex plugin marketplace for reusable design-pattern guidance.

This repository is intended to be hosted at `ByteDeskAI/design-pattern-references` and added to Claude Code as a marketplace:

```bash
claude plugin marketplace add ByteDeskAI/design-pattern-references
claude plugin install design-patterns@bytedesk-design-patterns
```

It can also be added to Codex as a marketplace:

```bash
codex plugin marketplace add ByteDeskAI/design-pattern-references
```

For local development from this checkout:

```bash
claude plugin validate .
claude plugin marketplace add .
claude plugin install design-patterns@bytedesk-design-patterns
codex plugin marketplace add .
```

## What Is Included

- A Claude Code marketplace manifest at `.claude-plugin/marketplace.json`.
- A Codex marketplace manifest at `.agents/plugins/marketplace.json`.
- One installable plugin at `plugins/design-patterns`.
- A source-neutral Markdown catalog of reusable design patterns.
- Pattern domains for object design, integration design, messaging, transformation, endpoints, operations, construction, structure, and collaboration.
- Architecture playbooks for recurring pattern combinations.
- Architecture smells for detecting design risks before recommending patterns.
- Language profiles for C#, Java, TypeScript, Python, Go, Rust, and C++.
- A bundled `patterns` CLI that Claude Code and Codex can use after the plugin is installed.

## Plugin Capability

After installation, Claude Code or Codex can use the `design-patterns` plugin when the user asks for pattern selection, architecture tradeoffs, refactoring guidance, or language-specific implementation approaches.

The plugin contributes:

- `skills/pattern-advisor/SKILL.md`: general model-invoked pattern guidance.
- `skills/pattern-finder/SKILL.md`: discover and compare candidate patterns from a problem statement.
- `skills/architecture-decision/SKILL.md`: produce ADR-style pattern decisions, tradeoffs, consequences, and verification plans.
- `skills/architecture-issue-scan/SKILL.md`: find design and integration issues in code or architecture notes.
- `skills/pattern-application/SKILL.md`: plan and apply a pattern-oriented refactor safely.
- `skills/integration-flow-review/SKILL.md`: review message-driven and integration flows.
- `agents/pattern-architect.md`: deeper architecture and design-review agent.
- `bin/patterns`: local catalog lookup helper.
- `data/patterns/*.md`: canonical Markdown pattern entries.
- `data/playbooks/*.md`: source-neutral pattern-composition playbooks.
- `data/smells/*.md`: source-neutral architecture smells and pattern responses.
- `data/languages/*.md`: canonical Markdown language profiles.
- `skills/*/references/{usages,examples,implementation,catalog}.md`: detailed skill documentation loaded on demand.

Each skill declares fully qualified skill frontmatter: `name`, `description`, `when_to_use`, `argument-hint`, invocation controls, conservative `allowed-tools`, and `model: inherit`.

## Catalog Model

The catalog is intentionally source-neutral. Patterns are organized by domain, category, group, and language applicability rather than by origin. New patterns can be added from any useful tradition, codebase, architecture review, or language ecosystem by adding a Markdown file under `plugins/design-patterns/data/patterns`.

Each pattern file uses frontmatter for machine filtering and Markdown sections for Claude-readable guidance. Pattern entries include decision metadata such as quality attributes, tradeoffs, failure modes, testing focus, observability focus, typed relationships, and implementation notes:

```text
---
slug: strategy
name: Strategy
domain: behavior-and-collaboration
category: Behavior and Collaboration
groups:
  - object-design
languages:
  - csharp
  - typescript
related:
  - state
relationships:
  - alternative:state
references:
  - skills/pattern-advisor/references/implementation.md
---

# Strategy

## Intent
...
```

Use the CLI to inspect the catalog:

```bash
plugins/design-patterns/bin/patterns domains
plugins/design-patterns/bin/patterns list object-design --language typescript
plugins/design-patterns/bin/patterns search router --scope integration-design --language typescript
plugins/design-patterns/bin/patterns recommend "duplicate delivery repeats side effects" --scope integration-design --language csharp
plugins/design-patterns/bin/patterns compare strategy state template-method
plugins/design-patterns/bin/patterns playbooks event-fanout
plugins/design-patterns/bin/patterns smells naive-exactly-once
plugins/design-patterns/bin/patterns show strategy --language csharp
plugins/design-patterns/bin/patterns languages go
```

## Architecture Guidance Model

The plugin now supports three layers of guidance:

- Patterns: individual reusable design responses.
- Playbooks: source-neutral combinations of patterns for recurring architecture situations.
- Smells: detectable design risks with pattern or no-pattern responses.

Skills should use the catalog progressively: detect smells, select patterns or playbooks, compare alternatives, then produce decision-ready output with consequences, tests, observability, and rollback signals.

## Validation

Run the local validation script:

```bash
python3 scripts/validate_catalog.py
```

If Claude Code is installed, also run:

```bash
claude plugin validate .
```

Codex marketplace metadata is validated by `scripts/validate_catalog.py`.

Unit tests cover the catalog loader and CLI behavior:

```bash
python3 -m unittest
```

## Repository Layout

```text
.
├── .claude-plugin/
│   └── marketplace.json
├── .agents/
│   └── plugins/marketplace.json
├── plugins/
│   └── design-patterns/
│       ├── .claude-plugin/plugin.json
│       ├── .codex-plugin/plugin.json
│       ├── agents/pattern-architect.md
│       ├── bin/patterns
│       ├── data/
│       │   ├── languages/*.md
│       │   ├── patterns/*.md
│       │   ├── playbooks/*.md
│       │   └── smells/*.md
│       ├── lib/pattern_catalog.py
│       └── skills/
│           ├── architecture-decision/SKILL.md
│           ├── architecture-issue-scan/SKILL.md
│           ├── integration-flow-review/SKILL.md
│           ├── pattern-advisor/SKILL.md
│           ├── pattern-application/SKILL.md
│           └── pattern-finder/SKILL.md
└── scripts/validate_catalog.py
```

## Versioning

The marketplace and plugin versions move together. Bump both versions when publishing catalog or capability changes that users should receive through marketplace updates.
