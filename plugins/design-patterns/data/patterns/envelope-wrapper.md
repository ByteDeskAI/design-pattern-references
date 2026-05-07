---
slug: envelope-wrapper
name: Envelope Wrapper
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
  - message-translator
  - format-indicator
  - claim-check
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Envelope Wrapper

## Intent
Wrap existing payload data with headers or envelope structure required by the messaging system.

## When To Use
- Payloads need metadata, security, addressing, or protocol framing.
- Core business data should remain separate from transport concerns.
- Legacy payloads must move through modern infrastructure.

## Avoid When
- The wrapper obscures payload ownership or versioning.
- Nested envelopes accumulate across systems.
- Consumers parse transport metadata as business data.
