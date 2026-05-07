---
slug: request-reply
name: Request-Reply
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
  - return-address
  - correlation-identifier
  - remote-procedure-invocation
---

# Request-Reply

## Intent
Send a request message and receive a correlated response message.

## When To Use
- A caller needs a response but messaging infrastructure is still desired.
- Temporal decoupling, retries, or broker routing matter.
- Correlation and timeout behavior can be explicit.

## Avoid When
- A synchronous API would be simpler and reliable enough.
- Timeouts and duplicate replies cannot be handled.
- The flow creates hidden distributed transactions.
