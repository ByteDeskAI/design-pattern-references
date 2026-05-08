---
description: Recommend design patterns for an architecture force or problem
argument-hint: "help | <query> [--language <language>] [--scope <scope>] [--risk <risk>] [--limit <n>]"
---

# Patterns Recommend

Parse `$ARGUMENTS` into a `patterns_recommend` MCP call.

Help behavior:

- `/patterns-recommend help`, `/patterns-recommend --help`, or `/patterns-recommend -h` returns help only.
- Help must include purpose, usage, options, examples, backing MCP tool, and JSON argument mapping.
- Do not call `patterns_recommend` when the user asks for help.

Argument mapping:

- First quoted or unflagged text: `query` required.
- `--language <language>`: optional language filter. If omitted, infer it from codebase files, path hints, and prompt terms.
- `--scope <scope>`: optional catalog scope. If omitted, infer `object-design`, `integration-design`, a catalog domain, or `all` from codebase and prompt context.
- `--risk <risk>`: decision emphasis such as `balanced`, `operability`, or `simplicity`.
- `--limit <n>`: maximum recommendations.

Inference behavior:

- Do not ask for `--language` or `--scope` just because they are missing.
- Prefer explicit arguments when supplied.
- Otherwise infer from nearby project files, stack markers, path names, and the problem statement.
- If evidence is ambiguous, use `all` for scope and omit the language filter.

Examples:

```text
/patterns-recommend "add a new SCM provider without changing rule execution code" --limit 5
/patterns-recommend "streaming job events to multiple UI consumers"
/patterns-recommend "duplicate delivery repeats side effects" --risk operability
```

Return the highest-signal recommendations with why they matched, when they might be wrong, and the smallest next design move.
