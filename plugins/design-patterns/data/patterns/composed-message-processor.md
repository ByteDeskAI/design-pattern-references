---
slug: composed-message-processor
name: Composed Message Processor
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
  - splitter
  - aggregator
  - scatter-gather
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Composed Message Processor

## Intent
Split, route, process, and reassemble a compound message while preserving the overall flow.

## When To Use
- Different parts of a message require different processing paths.
- A final combined result is needed.
- The processing topology can be made observable.

## Avoid When
- The composition hides too much stateful orchestration.
- A simple service can process the whole payload.
- Failure policy for partial work is undefined.
