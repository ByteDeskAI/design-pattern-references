---
slug: message-expiration
name: Message Expiration
domain: message-construction
category: Message Construction
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
  - dead-letter-channel
  - message-filter
  - control-bus
---

# Message Expiration

## Intent
Mark messages with a time after which processing is no longer useful.

## When To Use
- Stale work could cause wrong or wasteful side effects.
- Business deadlines or SLAs define useful processing windows.
- Queues may build up during outages.

## Avoid When
- Late messages must still be audited or compensated.
- Expiration policy conflicts with guaranteed delivery expectations.
- Clock skew and timezone handling are unmanaged.
