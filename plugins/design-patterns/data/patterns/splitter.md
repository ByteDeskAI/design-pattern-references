---
slug: splitter
name: Splitter
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
  - aggregator
  - message-sequence
  - composed-message-processor
---

# Splitter

## Intent
Break one compound message into multiple messages for independent processing.

## When To Use
- A payload contains independent items.
- Items can be processed, retried, or routed separately.
- Downstream components expect smaller units of work.

## Avoid When
- Items require one shared transaction.
- Reassembly semantics are unclear.
- Splitting loses context needed downstream.
