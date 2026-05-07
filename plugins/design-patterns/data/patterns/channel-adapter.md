---
slug: channel-adapter
name: Channel Adapter
domain: message-channel
category: Messaging Channels
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
  - messaging-gateway
  - adapter
  - message-endpoint
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Channel Adapter

## Intent
Connect a non-messaging application or resource to a messaging channel.

## When To Use
- A file, database, API, or device must participate in message flow.
- The adapter can isolate polling, serialization, and error policy.
- The application should remain unaware of broker details.

## Avoid When
- The adapter owns too much business logic.
- Backpressure and retry behavior are not designed.
- A native integration already exists.
