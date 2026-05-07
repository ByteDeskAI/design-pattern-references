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
