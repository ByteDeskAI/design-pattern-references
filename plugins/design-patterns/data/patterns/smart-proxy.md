---
slug: smart-proxy
name: Smart Proxy
domain: operations-and-observability
category: System Management
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
  - request-reply
  - return-address
  - correlation-identifier
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Smart Proxy

## Intent
Intercept request-reply conversations to preserve correlation or routing information across intermediaries.

## When To Use
- Intermediaries rewrite message IDs or reply addresses.
- The original requester still needs a coherent response.
- Correlation state can be stored and expired safely.

## Avoid When
- The proxy becomes a hidden dependency for all replies.
- State cleanup is unreliable.
- Direct preservation of headers would be simpler.
