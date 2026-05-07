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
