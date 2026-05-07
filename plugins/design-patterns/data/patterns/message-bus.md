---
slug: message-bus
name: Message Bus
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
  - canonical-data-model
  - control-bus
  - messaging-bridge
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Message Bus

## Intent
Provide a shared messaging backbone with common contracts and integration conventions.

## When To Use
- Many applications need decoupled integration through common infrastructure.
- Governance can define contracts, schemas, security, and observability.
- New participants should join through standard adapters or endpoints.

## Avoid When
- Central infrastructure becomes a bottleneck for team autonomy.
- Contracts are not governed.
- A bus is used as a substitute for clear domain ownership.
