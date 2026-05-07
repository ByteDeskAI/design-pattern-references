---
slug: control-bus
name: Control Bus
domain: operations-and-observability
category: System Management
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
  - message-bus
  - wire-tap
  - test-message
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Control Bus

## Intent
Use a messaging channel for operational commands and telemetry about the messaging system.

## When To Use
- Operators need distributed control and status signals.
- Management commands should flow through controlled channels.
- Runtime components can publish health and metrics events.

## Avoid When
- Control messages share channels with business traffic without isolation.
- Authorization and audit are weak.
- Operations would be simpler through platform-native tooling.
