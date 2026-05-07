---
slug: competing-consumers
name: Competing Consumers
domain: message-endpoint
category: Messaging Endpoints
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
  - point-to-point-channel
  - idempotent-receiver
  - message-dispatcher
---

# Competing Consumers

## Intent
Run multiple consumers against one channel so work is distributed among them.

## When To Use
- Throughput should scale horizontally.
- Each message should be handled by one consumer instance.
- Processing is idempotent or broker locks are reliable.

## Avoid When
- Strict ordering per stream is required and not partitioned.
- Duplicate processing would cause unsafe side effects.
- Consumers contend for scarce downstream resources.
