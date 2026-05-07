---
slug: message-translator
name: Message Translator
domain: messaging-system
category: Messaging Systems
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
  - normalizer
  - canonical-data-model
  - envelope-wrapper
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Message Translator

## Intent
Convert a message from one schema or representation to another.

## When To Use
- Systems cannot share the same data contract.
- Transformation is a boundary concern.
- You need to isolate canonical and external formats.

## Avoid When
- Translation silently changes business meaning.
- Mapping rules are scattered across consumers.
- Schema ownership is unclear.
