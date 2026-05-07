---
slug: wire-tap
name: Wire Tap
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
  - message-history
  - message-store
  - detour
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Wire Tap

## Intent
Copy messages from a channel for monitoring, audit, or diagnostics without disturbing the main flow.

## When To Use
- Operators need visibility into live traffic.
- Copies can be secured, sampled, and retained appropriately.
- The main path must remain unaffected.

## Avoid When
- Taps expose sensitive payloads without controls.
- Diagnostics add meaningful latency or backpressure.
- Copied data is mistaken for authoritative processing.
