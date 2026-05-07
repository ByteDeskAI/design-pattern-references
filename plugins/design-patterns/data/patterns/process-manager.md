---
slug: process-manager
name: Process Manager
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
  - routing-slip
  - correlation-identifier
  - message-store
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Process Manager

## Intent
Coordinate a multi-step message-driven process whose next actions depend on state and events.

## When To Use
- A long-running business process spans services or time.
- The next step depends on prior outcomes.
- State, timeouts, compensation, and correlation need an owner.

## Avoid When
- The flow is a simple static pipeline.
- The manager becomes a central transaction substitute.
- Durable process state is not available.
