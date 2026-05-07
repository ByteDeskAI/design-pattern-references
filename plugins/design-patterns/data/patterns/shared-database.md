---
slug: shared-database
name: Shared Database
domain: integration-style
category: Integration Styles
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
  - messaging
  - canonical-data-model
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Shared Database

## Intent
Let multiple applications integrate through common database tables or views.

## When To Use
- Applications need consistent shared state and can tolerate tight schema coupling.
- A database is already the operational coordination point.
- Read-only reporting integration is the main need.

## Avoid When
- Independent deployment and ownership matter.
- Teams cannot coordinate schema changes safely.
- Business rules would be bypassed by direct table access.
