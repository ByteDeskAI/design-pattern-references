---
slug: aggregator
name: Aggregator
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
  - splitter
  - correlation-identifier
  - resequencer
---

# Aggregator

## Intent
Combine related messages into one result once a completion condition is met.

## When To Use
- Split or parallel work must be gathered into a coherent result.
- Correlation, completeness, and timeout rules are explicit.
- Partial results can be handled deliberately.

## Avoid When
- The aggregator cannot know when a group is complete.
- State storage and cleanup are not designed.
- Late or duplicate messages would corrupt results.
