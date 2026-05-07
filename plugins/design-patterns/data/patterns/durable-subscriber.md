---
slug: durable-subscriber
name: Durable Subscriber
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
  - publish-subscribe-channel
  - guaranteed-delivery
  - message-store
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Durable Subscriber

## Intent
Preserve pub-sub messages for a subscriber while it is disconnected.

## When To Use
- A subscriber must not miss messages during downtime.
- The broker supports durable subscriptions or consumer groups.
- Retention and replay windows are governed.

## Avoid When
- The subscriber only needs live notifications.
- Backlogs can grow without bounds.
- Replay would trigger unsafe duplicate effects.
