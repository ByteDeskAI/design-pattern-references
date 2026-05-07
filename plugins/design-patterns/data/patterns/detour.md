---
slug: detour
name: Detour
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
  - wire-tap
  - control-bus
  - message-router
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Detour

## Intent
Temporarily route messages through extra steps for validation, testing, or troubleshooting.

## When To Use
- A flow needs controlled inspection or alternate processing.
- Operators can enable and disable the route safely.
- The detour path preserves semantics and observability.

## Avoid When
- Temporary routing becomes permanent hidden behavior.
- Detours alter production messages unexpectedly.
- Change control and rollback are missing.
