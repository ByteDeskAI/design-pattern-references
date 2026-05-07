---
slug: messaging-mapper
name: Messaging Mapper
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
  - message-translator
  - messaging-gateway
  - adapter
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Messaging Mapper

## Intent
Map between domain objects and messaging representations.

## When To Use
- Domain models should remain independent of transport schemas.
- Mapping rules need tests and version awareness.
- Messages carry a different shape from domain objects.

## Avoid When
- Mapping duplicates the same schema without value.
- Domain objects leak transport metadata.
- Mapping logic is split across endpoints.
