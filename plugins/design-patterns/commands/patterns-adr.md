---
description: Generate an ADR-style seed backed by the pattern catalog
argument-hint: "help | <decision> [--language <language>] [--scope <scope>] [--status <status>]"
---

# Patterns ADR

Parse `$ARGUMENTS` into a `patterns_adr` MCP call.

Help behavior:

- `/patterns-adr help`, `/patterns-adr --help`, or `/patterns-adr -h` returns help only.
- Help must include purpose, usage, options, examples, backing MCP tool, and JSON argument mapping.
- Do not call `patterns_adr` when the user asks for help.

Argument mapping:

- First quoted or unflagged text: `query` required.
- `--language <language>`: implementation language.
- `--scope <scope>`: catalog scope.
- `--status <status>`: ADR status, default `Proposed`.

Examples:

```text
/patterns-adr "choosing between Registry and Chain of Responsibility for executor dispatch" --language python
/patterns-adr "durable SSE event storage: Redis vs PostgreSQL" --scope backend --status Proposed
/patterns-adr "message replay and dead-letter handling for order events" --language csharp --scope integration-design
```

Return a decision seed with context, options, recommendation, consequences, verification, and rollback signals.
