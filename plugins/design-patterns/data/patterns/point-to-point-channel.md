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
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
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
