---
slug: return-address
name: Return Address
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
  - request-reply
  - correlation-identifier
  - smart-proxy
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Return Address

## Intent
Tell a receiver where to send a reply.

## When To Use
- Reply destinations vary by requestor or conversation.
- The receiver should not hard-code response channels.
- Temporary or tenant-specific response channels are used.

## Avoid When
- Replies always go to a fixed channel.
- The return address is not authenticated or authorized.
- Dynamic destinations create routing complexity without benefit.
