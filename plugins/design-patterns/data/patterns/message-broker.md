---
slug: message-broker
name: Message Broker
domain: message-routing
category: Message Routing
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
  - message-router
  - message-translator
  - message-bus
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Message Broker

## Intent
Centralize routing, transformation, and mediation between message producers and consumers.

## When To Use
- Many systems need controlled integration mediation.
- Routing and translation rules should be managed centrally.
- The broker can provide consistent observability and policy.

## Avoid When
- A central broker becomes a monolith of integration logic.
- Teams lose ownership of contracts.
- Performance or availability depends on one chokepoint.
