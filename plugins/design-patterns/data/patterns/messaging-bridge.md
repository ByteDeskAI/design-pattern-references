---
slug: messaging-bridge
name: Messaging Bridge
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
  - message-translator
  - message-bus
  - channel-adapter
---

# Messaging Bridge

## Intent
Move messages between separate messaging systems while preserving useful semantics.

## When To Use
- Two brokers or protocols must interoperate.
- Migration requires traffic to flow across old and new systems.
- Teams need a controlled boundary between messaging domains.

## Avoid When
- Delivery guarantees differ and cannot be reconciled.
- The bridge hides loss of ordering, headers, or identity.
- A shared broker would be simpler.
