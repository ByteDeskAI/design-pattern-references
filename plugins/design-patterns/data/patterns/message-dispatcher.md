---
slug: message-dispatcher
name: Message Dispatcher
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
  - selective-consumer
  - event-driven-consumer
  - message-router
---

# Message Dispatcher

## Intent
Coordinate message delivery from one channel to multiple local handlers.

## When To Use
- Several handlers share one consumer connection.
- Dispatch policy should be local and explicit.
- Handlers can be selected by type, header, or predicate.

## Avoid When
- Dispatch duplicates broker routing badly.
- Handler failures affect unrelated handlers.
- A framework dispatcher already handles this cleanly.
