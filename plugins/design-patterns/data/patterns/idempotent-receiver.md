---
slug: idempotent-receiver
name: Idempotent Receiver
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
  - guaranteed-delivery
  - dead-letter-channel
  - transactional-client
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Idempotent Receiver

## Intent
Handle duplicate messages without repeating unsafe side effects.

## When To Use
- At-least-once delivery can produce duplicates.
- Retries and redelivery are expected.
- A stable message identity or business key exists.

## Avoid When
- The receiver cannot identify duplicates.
- Deduplication state grows without retention policy.
- The design assumes exactly-once behavior without proof.
