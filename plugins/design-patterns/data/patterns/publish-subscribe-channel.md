---
slug: publish-subscribe-channel
name: Publish-Subscribe Channel
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
  - event-message
  - durable-subscriber
  - observer
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Publish-Subscribe Channel

## Intent
Broadcast messages to multiple interested subscribers.

## When To Use
- Many consumers independently react to the same event.
- Producers should not know subscribers.
- New subscribers should be added without changing producers.

## Avoid When
- Only one consumer should act.
- Subscribers require strict global ordering.
- Unbounded fanout could overload downstream systems.
