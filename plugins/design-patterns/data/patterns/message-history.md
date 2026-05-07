---
slug: message-history
name: Message History
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
  - correlation-identifier
  - wire-tap
  - message-store
---

# Message History

## Intent
Record the components or steps a message has passed through.

## When To Use
- Troubleshooting needs route and processing lineage.
- Messages cross several routers or processors.
- History metadata can be bounded and privacy-safe.

## Avoid When
- History grows without limits.
- Metadata leaks sensitive topology or user information.
- Tracing infrastructure already captures the needed information.
