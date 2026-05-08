---
description: Query the typed pattern catalog graph and relationships
argument-hint: "[relationship-question] [--format json]"
---

# Patterns Graph

Parse `$ARGUMENTS` into a `patterns_graph` MCP call.

Argument mapping:

- Quoted or unflagged text: optional `query`.
- `--format json`: request graph-shaped output when the caller needs machine-readable relationships.

Examples:

```text
/patterns-graph
/patterns-graph "what patterns are related to observer"
/patterns-graph "what patterns mitigate naive exactly once"
/patterns-graph "which patterns are companions of content-based-router" --format json
```

Return graph answers with relationship types, linked slugs, and enough context to pick the next command.
