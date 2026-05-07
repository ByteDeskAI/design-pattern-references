---
slug: event-message
name: Event Message
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
  - publish-subscribe-channel
  - message-history
  - observer
---

# Event Message

## Intent
Announce that a meaningful fact or state transition occurred.

## When To Use
- Subscribers decide independently how to react.
- The producer should not know downstream workflows.
- Events can be named in business language.

## Avoid When
- The sender needs to tell a specific receiver what to do.
- Events expose internal implementation noise.
- Consumers need data not included or reachable from the event.
