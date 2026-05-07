---
slug: routing-slip
name: Routing Slip
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
  - process-manager
  - dynamic-router
  - message-history
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Routing Slip

## Intent
Attach the remaining processing steps to the message so it can move through a variable route.

## When To Use
- The processing path is decided before or during execution.
- Each step can read and advance the route instructions.
- The flow should avoid a central orchestrator for every hop.

## Avoid When
- Routes need central policy checks at every step.
- Messages can be tampered with or route instructions cannot be trusted.
- A workflow engine would make state and compensation clearer.
