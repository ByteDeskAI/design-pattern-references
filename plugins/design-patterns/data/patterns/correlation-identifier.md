---
slug: correlation-identifier
name: Correlation Identifier
domain: message-construction
category: Message Construction
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
  - message-history
  - smart-proxy
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Correlation Identifier

## Intent
Attach an identifier that connects related messages in a conversation.

## When To Use
- Requests, replies, retries, or workflow steps must be tied together.
- Logs and traces need a shared business or technical key.
- Multiple in-flight conversations can overlap.

## Avoid When
- Identifiers are regenerated at every hop.
- Correlation leaks sensitive user data.
- The ID is confused with idempotency or causation.
