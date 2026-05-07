---
description: Use when the user wants to apply a design pattern to existing code, plan a pattern-oriented refactor, or generate language-specific implementation steps.
---

# Pattern Application

Use this skill to move from pattern choice to a safe implementation.

Before changing code:

1. Confirm the actual force being addressed.
2. Inspect the current files and tests.
3. Look up the selected pattern with `patterns show <slug>`.
4. Check `patterns languages <language>` or `data/languages/<language>.md` for stack idioms.
5. Identify the smallest boundary where the pattern can live.

Implementation rules:

- Keep the first refactor narrow and reversible.
- Preserve public behavior unless the user asks for behavior change.
- Add seams around variation points, not around everything.
- Keep names domain-specific; avoid generic names like `ConcreteStrategy` in production code.
- Add tests at the behavior boundary, not only class-construction tests.
- For messaging patterns, include retry, idempotency, correlation, observability, and dead-letter behavior where relevant.

Recommended output when planning:

1. Target pattern and why it fits.
2. Files or modules to change.
3. Step-by-step migration.
4. Compatibility and rollback notes.
5. Tests and runtime checks.

Recommended output when implementing:

1. Make the smallest coherent patch.
2. Run existing focused tests.
3. Explain the new collaboration shape with file references.
4. Call out follow-up refactors separately from the completed change.
