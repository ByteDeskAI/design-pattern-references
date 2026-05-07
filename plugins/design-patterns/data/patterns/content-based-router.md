---
slug: content-based-router
name: Content-Based Router
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
  - message-router
  - message-filter
  - recipient-list
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Content-Based Router

## Intent
Choose a destination by inspecting message content.

## When To Use
- Routing follows business data or headers.
- Producers should not know routing destinations.
- Routing rules can be tested and observed centrally.

## Avoid When
- Rules duplicate domain decisions that belong upstream.
- Payload inspection is expensive or privacy-sensitive.
- Routes change so often that operations cannot reason about flow.
