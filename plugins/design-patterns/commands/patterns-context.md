---
description: Build a model-ready pattern context pack for code and a design question
argument-hint: "<path> --query <problem> [--language <language>] [--scope <scope>]"
---

# Patterns Context

Parse `$ARGUMENTS` into a `patterns_context` MCP call.

Argument mapping:

- First positional value: `path` required.
- `--query <problem>`: design question or feature context required.
- `--language <language>`: implementation language.
- `--scope <scope>`: catalog scope.

Examples:

```text
/patterns-context backend/app/providers/ai --query "adding a new AI provider safely" --language python --scope backend
/patterns-context frontend/src/state --query "managing streaming job state" --language typescript --scope frontend
/patterns-context services/orders --query "duplicate message handling and replay" --language csharp --scope integration-design
```

Return a compact context pack: scan findings, recommendations, relevant snippets, and an ADR seed when useful.
