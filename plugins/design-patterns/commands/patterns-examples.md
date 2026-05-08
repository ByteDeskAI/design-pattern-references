---
description: Show copyable Design Patterns slash commands and MCP request examples
argument-hint: "[topic-or-empty]"
---

# Design Patterns MCP Examples

Return copyable slash commands, not descriptions of MCP schemas.

If the user asks for "example MCP requests", "how do I call the design patterns tool", or similar wording, answer with `/patterns-*` commands first. Keep tool names and parameter schema explanations secondary.

Call the `patterns_examples` MCP tool when available. If the tool is unavailable, use the examples below directly.

Use this response shape:

```text
/patterns-examples [topic]
/patterns-recommend "<architecture force or problem>" [--language <language>] [--scope <scope>] [--risk <risk>] [--limit <n>]
/patterns-scan <path> [--min-confidence <0-1>] [--include-docs] [--include-generated]
/patterns-context <path> --query "<problem>" [--language <language>] [--scope <scope>]
/patterns-simulate "<decision or competing options>" [--language <language>] [--risk <risk>] [--limit <n>]
/patterns-migrate "<current smell or source shape>" --to <target-pattern> [--language <language>] [--query "<context>"]
/patterns-snippets <pattern-slug>[,<pattern-slug>...] [--language <language>]
/patterns-adr "<architecture decision>" [--language <language>] [--scope <scope>] [--status <status>]
/patterns-graph ["relationship question"] [--format json]
```

Examples:

```text
/patterns-recommend "add a new SCM provider without changing rule execution code" --language python --scope backend --limit 5
/patterns-scan backend/app/workflow_engine --min-confidence 0.45
/patterns-context backend/app/providers/ai --query "adding a new AI provider safely" --language python --scope backend
/patterns-simulate "Strategy vs Chain of Responsibility for AI provider failover" --language python --risk operability
/patterns-migrate "hardcoded if/elif provider selection" --to strategy --language python
/patterns-snippets strategy,idempotent-receiver --language python
/patterns-adr "durable event storage for SSE replay: Redis vs PostgreSQL" --language python --scope backend
/patterns-graph "what patterns mitigate naive exactly once"
```

If a user asks for raw MCP payloads, include the corresponding tool and arguments after the slash command:

```text
/patterns-recommend "duplicate delivery repeats side effects" --language python
MCP tool: patterns_recommend
Arguments: {"query":"duplicate delivery repeats side effects","language":"python"}
```
