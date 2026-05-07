---
slug: message-filter
name: Message Filter
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
  - invalid-message-channel
  - selective-consumer
  - content-based-router
---

# Message Filter

## Intent
Remove messages that do not meet criteria before they reach downstream processing.

## When To Use
- Consumers should only receive relevant messages.
- Filtering can reduce load and noise.
- Discarded messages are safe to drop or redirect.

## Avoid When
- Dropped messages require audit or compensation.
- Filter criteria are hidden business rules.
- Filtering masks producer contract problems.
