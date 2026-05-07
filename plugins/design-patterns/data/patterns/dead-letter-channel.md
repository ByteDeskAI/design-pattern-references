---
slug: dead-letter-channel
name: Dead Letter Channel
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
  - guaranteed-delivery
  - invalid-message-channel
  - idempotent-receiver
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Dead Letter Channel

## Intent
Preserve messages that cannot be delivered or processed after policy is exhausted.

## When To Use
- Failed delivery must be observable and recoverable.
- Retry policy has clear terminal conditions.
- Operations needs a place to inspect and replay poison messages.

## Avoid When
- Failures are silently ignored after dead-lettering.
- Replay would repeat unsafe side effects.
- Retention and access policy are undefined.
