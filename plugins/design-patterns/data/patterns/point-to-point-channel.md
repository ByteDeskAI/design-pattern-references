---
slug: point-to-point-channel
name: Point-to-Point Channel
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
  - competing-consumers
  - publish-subscribe-channel
---

# Point-to-Point Channel

## Intent
Deliver each message to one eligible receiver.

## When To Use
- Work items should be load-balanced across consumers.
- Only one consumer should perform the action.
- Horizontal scaling is needed without duplicate processing.

## Avoid When
- Every subscriber must see every message.
- Consumers cannot process idempotently.
- Ordering expectations conflict with parallelism.
