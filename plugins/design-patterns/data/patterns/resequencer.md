---
slug: resequencer
name: Resequencer
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
  - message-sequence
  - aggregator
  - message-store
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Resequencer

## Intent
Reorder related messages into the expected sequence before forwarding.

## When To Use
- Parallel or distributed processing can deliver messages out of order.
- Downstream consumers require ordered input.
- Sequence metadata and buffering policy are available.

## Avoid When
- Ordering is unnecessary or can be handled by the consumer.
- Missing messages would block indefinitely.
- Buffering introduces unacceptable latency.
