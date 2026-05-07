---
description: Use when reviewing code, architecture, PRs, diagrams, or design notes for pattern-related design issues, smells, missing seams, coupling, or integration risks.
---

# Architecture Issue Scan

Use this skill to find architecture and design issues that patterns can clarify or fix.

Scan for object-design issues:

- Repeated conditionals choosing behavior or types.
- Constructors that know too much about product families.
- God services, anemic wrappers, circular dependencies, and unstable abstractions.
- Inheritance used for configuration rather than behavior.
- Cross-cutting behavior duplicated instead of wrapped, pipelined, or decorated.
- Lifecycle state scattered across methods.

Scan for integration issues:

- Synchronous call chains where async messaging would reduce coupling.
- Missing idempotency for at-least-once delivery.
- No dead-letter, invalid-message, or retry terminal policy.
- Payloads with no version or format indicator.
- Routing rules spread across producers and consumers.
- No correlation identifiers, message history, or operational tap points.
- Oversized messages that should use claim check or message sequence.

Workflow:

1. Inspect the actual code or artifact before recommending changes.
2. Use `patterns search` to confirm candidate patterns.
3. Separate real findings from optional refactor ideas.
4. Prefer local idioms and framework capabilities over textbook ceremony.

For review-style output, lead with findings ordered by severity. For each finding include:

- Symptom.
- Why it matters.
- Pattern that addresses the force.
- Smallest safe next step.
- Test or observability check that would prove the fix.

Avoid naming patterns as decoration. If a pattern does not remove concrete risk, say no pattern is needed yet.

