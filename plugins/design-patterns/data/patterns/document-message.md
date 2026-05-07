---
slug: document-message
name: Document Message
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
  - event-message
  - claim-check
  - message-translator
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Document Message

## Intent
Transfer a document-like data structure for another system to consume.

## When To Use
- The receiver decides what to do with the data.
- The payload is a business document, snapshot, or data transfer.
- The message should not imply a specific action.

## Avoid When
- The producer needs the receiver to execute a command.
- Payload size exceeds broker or retention limits.
- Document versioning is unmanaged.
