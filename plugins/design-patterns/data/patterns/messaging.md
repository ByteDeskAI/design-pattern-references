---
slug: messaging
name: Messaging
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
  - message-channel
  - message-endpoint
  - guaranteed-delivery
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Messaging

## Intent
Integrate applications by sending messages through channels with temporal decoupling.

## When To Use
- Participants should not require each other to be available at the same instant.
- Workflows need buffering, routing, fanout, or retry.
- Loose coupling matters more than immediate response.

## Avoid When
- The interaction is a simple local call.
- Operational ownership for queues and consumers is missing.
- Message contracts and idempotency cannot be governed.
