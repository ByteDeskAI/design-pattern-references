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
