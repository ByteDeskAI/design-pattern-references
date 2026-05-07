---
slug: normalizer
name: Normalizer
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
  - canonical-data-model
  - message-translator
  - format-indicator
---

# Normalizer

## Intent
Transform different incoming formats into one common message shape.

## When To Use
- Multiple sources represent the same concept differently.
- Downstream components benefit from one canonical input.
- Source-specific mappings can be isolated and tested.

## Avoid When
- A single canonical shape loses important source distinctions.
- Mappings change faster than downstream consumers can tolerate.
- Normalization logic becomes scattered.
