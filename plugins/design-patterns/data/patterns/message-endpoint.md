---
slug: message-endpoint
name: Message Endpoint
domain: messaging-system
category: Messaging Systems
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
  - messaging-gateway
  - polling-consumer
  - event-driven-consumer
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Message Endpoint

## Intent
Connect application code to messaging infrastructure for sending or receiving.

## When To Use
- Business logic needs a boundary to messaging concerns.
- Endpoint code can handle serialization, acknowledgements, and errors.
- Testing requires separation from broker details.

## Avoid When
- Broker APIs leak throughout domain code.
- Endpoint lifecycle is unmanaged.
- Error handling is inconsistent.
