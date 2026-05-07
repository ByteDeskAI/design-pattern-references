---
slug: event-driven-consumer
name: Event-Driven Consumer
domain: message-endpoint
category: Messaging Endpoints
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
  - polling-consumer
  - message-dispatcher
  - competing-consumers
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Event-Driven Consumer

## Intent
Invoke consumer logic automatically when messages arrive.

## When To Use
- The system should react quickly to new messages.
- The runtime can manage listener lifecycle and concurrency.
- Backpressure and error handling are explicit.

## Avoid When
- The consumer cannot handle bursts.
- Processing needs carefully scheduled windows.
- Listener failures are hard to observe.
