---
slug: polling-consumer
name: Polling Consumer
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
  - event-driven-consumer
  - competing-consumers
  - message-endpoint
---

# Polling Consumer

## Intent
Let an application request messages when it is ready to process them.

## When To Use
- The consumer needs control over timing or rate.
- Batching or scheduled processing is useful.
- Infrastructure does not push messages.

## Avoid When
- Low latency is required.
- Polling wastes resources or causes uneven load.
- Backoff and concurrency are unmanaged.
