---
slug: datatype-channel
name: Datatype Channel
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
  - message
  - message-filter
  - format-indicator
---

# Datatype Channel

## Intent
Separate channels by message type so receivers know what kind of payload to expect.

## When To Use
- Type-specific consumers simplify validation and routing.
- Operational ownership differs by message type.
- Schema evolution needs channel-level clarity.

## Avoid When
- Too many narrow channels create management overhead.
- Consumers still need runtime type guessing.
- Message versioning is not handled.
