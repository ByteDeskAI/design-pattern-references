---
slug: canonical-data-model
name: Canonical Data Model
domain: message-transformation
category: Message Transformation
groups:
  - integration-design
languages:
  - csharp
  - java
  - typescript
  - python
  - go
  - rust
  - cpp
related:
  - normalizer
  - message-bus
  - message-translator
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Canonical Data Model

## Intent
Define a shared data representation that reduces pairwise transformations.

## When To Use
- Many systems exchange overlapping business concepts.
- A governed common model can lower integration complexity.
- Domain ownership and versioning can be managed.

## Avoid When
- The canonical model becomes a lowest-common-denominator enterprise schema.
- Teams cannot govern changes.
- Local bounded contexts need different meanings for the same terms.
