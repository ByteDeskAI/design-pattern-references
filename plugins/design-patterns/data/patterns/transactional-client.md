---
slug: transactional-client
name: Transactional Client
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
  - idempotent-receiver
  - message-store
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Transactional Client

## Intent
Coordinate message send or receive work with transactional boundaries.

## When To Use
- Message acknowledgement and local state changes must be coordinated.
- The messaging system supports transactions or reliable outbox/inbox patterns.
- Failure behavior can be tested under retries.

## Avoid When
- Distributed transactions are assumed but unsupported.
- Side effects outside the transaction are not idempotent.
- Transaction scope is too broad.
