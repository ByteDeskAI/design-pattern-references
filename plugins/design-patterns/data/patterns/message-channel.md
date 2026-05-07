---
slug: message-channel
name: Message Channel
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
  - point-to-point-channel
  - publish-subscribe-channel
  - datatype-channel
---

# Message Channel

## Intent
Provide a logical path that carries messages from senders to receivers.

## When To Use
- Applications need a named communication path.
- The channel can express ownership, delivery mode, and contract expectations.
- Consumers should subscribe to a stable address rather than concrete senders.

## Avoid When
- Channel proliferation hides ownership.
- Naming does not encode message semantics.
- Security and retention policy are undefined.
