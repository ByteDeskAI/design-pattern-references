---
slug: remote-procedure-invocation
name: Remote Procedure Invocation
domain: integration-style
category: Integration Styles
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
  - request-reply
  - service-activator
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Remote Procedure Invocation

## Intent
Expose application behavior through synchronous remote calls.

## When To Use
- The caller needs an immediate response.
- Latency and availability are acceptable for request-time coupling.
- The remote API represents a stable capability boundary.

## Avoid When
- Call chains can amplify latency or outages.
- Work should continue asynchronously.
- Retries are not idempotent or observable.
