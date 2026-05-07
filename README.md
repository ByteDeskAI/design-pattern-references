# Design Pattern References

Claude Code plugin marketplace for reusable design-pattern guidance.

This repository is intended to be hosted at `ByteDeskAI/design-pattern-references` and added to Claude Code as a marketplace:

```bash
claude plugin marketplace add ByteDeskAI/design-pattern-references
claude plugin install design-patterns@bytedesk-design-patterns
```

For local development from this checkout:

```bash
claude plugin validate .
claude plugin marketplace add .
claude plugin install design-patterns@bytedesk-design-patterns
```

## What Is Included

- A Claude Code marketplace manifest at `.claude-plugin/marketplace.json`.
- One installable plugin at `plugins/design-patterns`.
- Structured catalogs for all 23 Gang of Four patterns.
- Structured catalog entries for the Enterprise Integration Patterns messaging catalog.
- Language-specific GoF implementation notes for C#, Java, TypeScript, Python, Go, Rust, and C++.
- A bundled `patterns` CLI that Claude can use after the plugin is installed.

## Plugin Capability

After installation, Claude can use the `design-patterns` plugin when the user asks for pattern selection, architecture tradeoffs, refactoring guidance, or language-specific implementation approaches.

The plugin contributes:

- `skills/pattern-advisor/SKILL.md`: general model-invoked pattern guidance.
- `skills/pattern-finder/SKILL.md`: discover and compare candidate patterns from a problem statement.
- `skills/architecture-issue-scan/SKILL.md`: find design and integration issues in code or architecture notes.
- `skills/pattern-application/SKILL.md`: plan and apply a pattern-oriented refactor safely.
- `skills/integration-flow-review/SKILL.md`: review message-driven flows with Enterprise Integration Patterns.
- `agents/pattern-architect.md`: deeper architecture and design-review agent.
- `bin/patterns`: local catalog lookup helper.
- `data/gof.json`, `data/eip.json`, and `data/languages.json`: the bundled reference catalogs.

## Catalog Sources

The GoF catalog uses the canonical 23 pattern names and categories from *Design Patterns: Elements of Reusable Object-Oriented Software*. The Enterprise Integration Patterns catalog is based on the public messaging table of contents at [enterpriseintegrationpatterns.com](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).

Descriptions, selection guidance, implementation notes, and language guidance in this repository are original summaries written for this plugin. They are not copied from the source books or website.

## Validation

Run the local validation script:

```bash
python3 scripts/validate_catalog.py
```

If Claude Code is installed, also run:

```bash
claude plugin validate .
```

## Repository Layout

```text
.
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── design-patterns/
│       ├── .claude-plugin/plugin.json
│       ├── agents/pattern-architect.md
│       ├── bin/patterns
│       ├── data/
│       │   ├── eip.json
│       │   ├── gof.json
│       │   └── languages.json
│       └── skills/
│           ├── architecture-issue-scan/SKILL.md
│           ├── integration-flow-review/SKILL.md
│           ├── pattern-advisor/SKILL.md
│           ├── pattern-application/SKILL.md
│           └── pattern-finder/SKILL.md
└── scripts/validate_catalog.py
```

## Versioning

The marketplace and plugin both start at `0.1.0`. Bump both versions when publishing catalog or capability changes that users should receive through marketplace updates.
