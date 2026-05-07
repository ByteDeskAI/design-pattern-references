---
slug: guaranteed-delivery
name: Guaranteed Delivery
domain: message-channel
category: Messaging Channels
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
  - dead-letter-channel
  - message-store
  - idempotent-receiver
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Guaranteed Delivery

## Intent
Persist messages so they can survive process or broker interruptions until delivery policy completes.

## When To Use
- Message loss is unacceptable.
- Durable storage and acknowledgements are available.
- Receivers are idempotent or side effects are controlled.

## Avoid When
- Low latency is more important than durability.
- Duplicate delivery cannot be tolerated or mitigated.
- Operational storage limits are unknown.
