---
slug: dynamic-router
name: Dynamic Router
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
  - recipient-list
  - routing-slip
  - control-bus
---

# Dynamic Router

## Intent
Route messages using destinations that can change at runtime.

## When To Use
- Receivers join, leave, or advertise capabilities dynamically.
- Static routing tables are too brittle.
- Runtime discovery is governed and observable.

## Avoid When
- Dynamic registration can be spoofed or stale.
- Operators cannot predict where messages flow.
- Static routing would be simpler and safer.
