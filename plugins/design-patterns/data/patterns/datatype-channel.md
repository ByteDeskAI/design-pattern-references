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
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
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
