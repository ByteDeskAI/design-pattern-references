---
slug: content-filter
name: Content Filter
domain: message-transformation
category: Message Transformation
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
  - content-enricher
  - claim-check
  - message-filter
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Content Filter

## Intent
Remove unneeded data from a message before forwarding it.

## When To Use
- Downstream systems need only a subset of the payload.
- Privacy, bandwidth, or contract clarity requires trimming fields.
- The filtered message remains semantically complete for its purpose.

## Avoid When
- Filtering removes data needed for auditing or compensation.
- Each consumer defines its own incompatible subset.
- The transformation masks an oversized canonical model.
