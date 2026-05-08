---
description: Plan a migration from a current smell or shape to a target pattern
argument-hint: "<source> --to <target-pattern> [--language <language>] [--query <context>]"
---

# Patterns Migrate

Parse `$ARGUMENTS` into a `patterns_migrate` MCP call.

Argument mapping:

- First quoted or unflagged text: `source` required.
- `--to <target-pattern>`: `target` required.
- `--language <language>`: implementation language.
- `--query <context>`: extra project context.

Examples:

```text
/patterns-migrate "hardcoded if/elif provider selection" --to strategy --language python
/patterns-migrate "fat router with inline persistence and branching" --to facade --language typescript
/patterns-migrate provider-switch-sprawl --to bridge --query "providers are GitHub, GitLab, and Bitbucket"
```

Return a staged migration plan with behavior-preserving tests, rollback points, and over-patterning warnings.
