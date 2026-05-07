---
slug: messaging-gateway
name: Messaging Gateway
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
  - messaging-mapper
  - channel-adapter
  - facade
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Messaging Gateway

## Intent
Expose messaging operations through an application-facing interface.

## When To Use
- Domain code should not depend on broker APIs.
- Sending and receiving policies need a testable abstraction.
- Application code benefits from task-oriented messaging methods.

## Avoid When
- The gateway hides important asynchronous failure semantics.
- It becomes a general service locator.
- Broker-specific behavior leaks through anyway.
