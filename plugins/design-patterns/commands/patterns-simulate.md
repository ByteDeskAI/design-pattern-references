---
description: Score pattern options against architecture decision criteria
argument-hint: "help | <decision-or-options> [--language <language>] [--risk <risk>] [--limit <n>]"
---

# Patterns Simulate

Parse `$ARGUMENTS` into a `patterns_simulate` MCP call.

Help behavior:

- `/patterns-simulate help`, `/patterns-simulate --help`, or `/patterns-simulate -h` returns help only.
- Help must include purpose, usage, options, examples, backing MCP tool, and JSON argument mapping.
- Do not call `patterns_simulate` when the user asks for help.

Argument mapping:

- First quoted or unflagged text: `query` required.
- `--language <language>`: implementation language.
- `--risk <risk>`: scorecard emphasis.
- `--limit <n>`: number of options to score.

Examples:

```text
/patterns-simulate "Strategy vs Chain of Responsibility for AI provider failover" --language python --risk operability
/patterns-simulate "Command vs State for workflow node execution lifecycle" --language typescript
/patterns-simulate "event fanout with replay and dead-letter handling" --language csharp --limit 4
```

Return a scorecard-style comparison, the recommended option, and the signals that would change the decision.
