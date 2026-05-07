---
slug: service-activator
name: Service Activator
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
  - command-message
  - messaging-gateway
  - adapter
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Service Activator

## Intent
Invoke application service behavior in response to a message.

## When To Use
- Existing service logic should be available through messaging.
- Endpoint code can translate messages into service calls.
- The same service may be invoked through other transports.

## Avoid When
- The message model forces service methods into poor shapes.
- Service calls are not idempotent under retries.
- Transport concerns leak into the service API.
