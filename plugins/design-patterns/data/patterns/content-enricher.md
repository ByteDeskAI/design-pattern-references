---
slug: content-enricher
name: Content Enricher
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
  - content-filter
  - claim-check
  - message-translator
---

# Content Enricher

## Intent
Add missing data to a message before downstream processing.

## When To Use
- The sender lacks data required by the receiver.
- Enrichment data has a clear authoritative source.
- Latency, cache policy, and failure behavior are acceptable.

## Avoid When
- Enrichment hides missing upstream contract ownership.
- External lookups make flow unreliable without fallback.
- Sensitive data is added unnecessarily.
