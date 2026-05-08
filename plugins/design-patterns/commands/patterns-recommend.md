---
description: Recommend design patterns for an architecture force or problem
argument-hint: "<query> [--language <language>] [--scope <scope>] [--risk <risk>] [--limit <n>]"
---

# Patterns Recommend

Parse `$ARGUMENTS` into a `patterns_recommend` MCP call.

Argument mapping:

- First quoted or unflagged text: `query` required.
- `--language <language>`: language filter.
- `--scope <scope>`: catalog scope such as `object-design`, `integration-design`, `backend`, `frontend`, or `all`.
- `--risk <risk>`: decision emphasis such as `balanced`, `operability`, or `simplicity`.
- `--limit <n>`: maximum recommendations.

Examples:

```text
/patterns-recommend "add a new SCM provider without changing rule execution code" --language python --scope backend --limit 5
/patterns-recommend "streaming job events to multiple UI consumers" --language typescript --scope frontend
/patterns-recommend "duplicate delivery repeats side effects" --scope integration-design --risk operability
```

Return the highest-signal recommendations with why they matched, when they might be wrong, and the smallest next design move.
