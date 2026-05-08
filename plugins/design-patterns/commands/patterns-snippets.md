---
description: Fetch language-specific implementation snippets for pattern slugs
argument-hint: "help | <pattern-slug>[,<pattern-slug>...] [--language <language>]"
---

# Patterns Snippets

Parse `$ARGUMENTS` into a `patterns_snippets` MCP call.

Help behavior:

- `/patterns-snippets help`, `/patterns-snippets --help`, or `/patterns-snippets -h` returns help only.
- Help must include purpose, usage, options, examples, backing MCP tool, and JSON argument mapping.
- Do not call `patterns_snippets` when the user asks for help.

Argument mapping:

- First positional value: comma-separated pattern slugs required.
- `--language <language>`: implementation language filter.

Examples:

```text
/patterns-snippets strategy --language python
/patterns-snippets strategy,idempotent-receiver --language python
/patterns-snippets content-based-router,dead-letter-channel --language csharp
```

Return snippets only when they are relevant to the requested language and pattern. Include the catalog slugs so the user can chain into `/patterns-context` or `/patterns-migrate`.
