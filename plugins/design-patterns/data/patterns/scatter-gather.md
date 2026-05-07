---
slug: scatter-gather
name: Scatter-Gather
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
  - recipient-list
  - aggregator
  - request-reply
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Scatter-Gather

## Intent
Send a request to multiple recipients and aggregate their replies.

## When To Use
- Several providers can answer or enrich the same request.
- The caller benefits from parallelism or best-result selection.
- Timeout and partial-response rules are explicit.

## Avoid When
- Every recipient must succeed transactionally.
- Response fan-in would overload the aggregator.
- Provider behavior cannot be made idempotent.
