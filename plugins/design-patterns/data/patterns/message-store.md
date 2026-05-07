---
slug: message-store
name: Message Store
domain: operations-and-observability
category: System Management
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
  - wire-tap
  - message-history
  - dead-letter-channel
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Message Store

## Intent
Persist messages or selected metadata for audit, replay, analytics, or diagnostics.

## When To Use
- Transient broker traffic must be queried later.
- Replay, reconciliation, or compliance requires retained records.
- Retention, masking, and access policy are explicit.

## Avoid When
- The store becomes an ungoverned shadow database.
- Payload retention violates privacy or cost constraints.
- Replay semantics are unsafe.
