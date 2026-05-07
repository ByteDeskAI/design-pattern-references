---
description: Use when selecting, comparing, applying, or reviewing Gang of Four design patterns or Enterprise Integration Patterns, especially when the user asks for language-specific implementation guidance.
---

# Pattern Advisor

Use this skill to help users select, compare, implement, or review established software design patterns.

Prefer the bundled structured catalogs over memory:

- `data/gof.json` covers the 23 Gang of Four patterns with language notes.
- `data/eip.json` covers Enterprise Integration Patterns from the messaging catalog.
- `data/languages.json` summarizes language and ecosystem idioms.
- The executable `patterns` is available on `PATH` after installation and can list, search, or show catalog entries.

When advising:

1. Start from the user's actual forces: coupling, variability, ownership, runtime constraints, failure modes, observability, testing, and team skill.
2. Identify whether the problem is object design, system integration, or both.
3. Recommend one primary pattern and at most two alternatives unless the user asks for a broader survey.
4. Include language-specific implementation advice when a language or framework is known.
5. Call out when a pattern is likely overkill, hiding a simpler language feature or framework primitive.
6. For Enterprise Integration Patterns, include delivery semantics, idempotency, retry/dead-letter behavior, message shape, and observability considerations.
7. For GoF patterns, include the collaboration shape, dependency direction, test seams, and common misuses.
8. Avoid copying source-book prose; summarize in fresh, practical language.

Useful lookup commands:

```bash
patterns list gof
patterns list eip
patterns search "router"
patterns show strategy
patterns show content-based-router
patterns languages
```

