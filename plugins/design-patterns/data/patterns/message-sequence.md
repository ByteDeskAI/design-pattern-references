---
slug: message-sequence
name: Message Sequence
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
  - splitter
  - aggregator
  - resequencer
---

# Message Sequence

## Intent
Split related data across multiple ordered messages with enough metadata to reconstruct context.

## When To Use
- Payloads are too large or naturally chunked.
- Receivers need sequence number, total count, or completion markers.
- Streaming or partial processing is useful.

## Avoid When
- A claim check or external object store is simpler.
- Ordering cannot be preserved or repaired.
- Receivers cannot handle missing chunks.
