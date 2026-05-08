---
description: Scan a file or directory for pattern-relevant architecture smells
argument-hint: "help | <path> [--min-confidence <0-1>] [--pack <pack>] [--include-docs] [--include-generated]"
---

# Patterns Scan

Parse `$ARGUMENTS` into a `patterns_scan` MCP call.

Help behavior:

- `/patterns-scan help`, `/patterns-scan --help`, or `/patterns-scan -h` returns help only.
- Help must include purpose, usage, options, examples, backing MCP tool, and JSON argument mapping.
- Do not call `patterns_scan` when the user asks for help.

Argument mapping:

- First positional value: `path` required.
- `--min-confidence <0-1>`: filter weak findings.
- `--pack <pack>`: smell rule pack, default `all`.
- `--include-docs`: include documentation files in the scan.
- `--include-generated`: include generated files.

Examples:

```text
/patterns-scan backend/app/repositories/jobs.py --min-confidence 0.5
/patterns-scan backend/app/workflow_engine --min-confidence 0.45
/patterns-scan docs/architecture --include-docs --pack integration
```

Lead with concrete findings. For each finding, include the smell, why it matters, likely pattern response, and a small next check.
