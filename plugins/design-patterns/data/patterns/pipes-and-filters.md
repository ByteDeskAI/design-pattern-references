---
slug: pipes-and-filters
name: Pipes and Filters
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
  - message-router
  - message-translator
  - composed-message-processor
---

# Pipes and Filters

## Intent
Process data through independent steps connected by channels.

## When To Use
- A flow can be decomposed into reusable transformations or decisions.
- Steps should scale, test, and deploy independently.
- Intermediate results are useful for troubleshooting.

## Avoid When
- The flow requires tight shared transactions.
- Every step depends on hidden mutable context.
- Operational overhead outweighs decomposition benefits.
