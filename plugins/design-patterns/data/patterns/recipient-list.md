---
slug: recipient-list
name: Recipient List
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
  - publish-subscribe-channel
  - scatter-gather
  - content-based-router
---

# Recipient List

## Intent
Route one message to a computed list of recipients.

## When To Use
- Fanout targets depend on message content or configuration.
- Recipients are selected per message.
- The sender should not manage every destination.

## Avoid When
- All subscribers should receive every message.
- Recipient computation is expensive or opaque.
- Partial delivery semantics are undefined.
