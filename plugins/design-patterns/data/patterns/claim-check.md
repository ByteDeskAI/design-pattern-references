---
slug: claim-check
name: Claim Check
domain: message-transformation
category: Message Transformation
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
  - message-sequence
  - content-filter
  - message-store
---

# Claim Check

## Intent
Store bulky data elsewhere and send a reference through the message flow.

## When To Use
- Payloads are too large or sensitive for the broker.
- Consumers can dereference the payload with proper authorization.
- Lifecycle and cleanup of stored content are managed.

## Avoid When
- The referenced data may disappear before consumption.
- Access control cannot be enforced.
- The reference creates tight coupling to storage internals.
