---
slug: message
name: Message
domain: messaging-system
category: Messaging Systems
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
  - command-message
  - document-message
  - event-message
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Message

## Intent
Package data and metadata as a unit exchanged through a channel.

## When To Use
- A sender needs to communicate facts, commands, documents, or events.
- Headers and payload should travel together.
- The message can be versioned and validated independently.

## Avoid When
- Payloads are too large for the broker.
- Metadata needed for operations is missing.
- Message meaning depends on hidden sender state.
