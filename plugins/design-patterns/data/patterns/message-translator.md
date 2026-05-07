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
