---
slug: test-message
name: Test Message
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
  - control-bus
  - detour
  - invalid-message-channel
---

# Test Message

## Intent
Send known diagnostic messages through the system to verify behavior.

## When To Use
- Operators need live confidence that routes and consumers work.
- Synthetic traffic can be identified and isolated.
- Health checks should exercise the real messaging path.

## Avoid When
- Test messages can trigger real business side effects.
- Synthetic traffic is indistinguishable from production data.
- The checks create noise or false confidence.
