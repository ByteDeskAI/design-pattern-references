---
slug: selective-consumer
name: Selective Consumer
domain: message-endpoint
category: Messaging Endpoints
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
  - message-filter
  - datatype-channel
  - message-dispatcher
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Selective Consumer

## Intent
Let a consumer receive only messages that match selection criteria.

## When To Use
- Filtering at the broker or endpoint reduces unnecessary work.
- Selection can be expressed in headers or broker-supported predicates.
- Consumers own clear subscriptions.

## Avoid When
- Filtering requires expensive payload inspection.
- Selection rules hide business routing.
- A separate channel per type would be clearer.
