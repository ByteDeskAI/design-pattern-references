---
slug: message-router
name: Message Router
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
  - content-based-router
  - recipient-list
  - dynamic-router
---

# Message Router

## Intent
Route a message to one or more destinations based on routing logic.

## When To Use
- Senders should not know all possible recipients.
- Routing criteria may change independently of producers.
- Central routing improves control and observability.

## Avoid When
- Routing rules become opaque business logic.
- A direct subscription model is enough.
- The router is a bottleneck or single point of failure.
