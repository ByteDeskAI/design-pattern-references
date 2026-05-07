---
slug: command-message
name: Command Message
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
  - command
  - request-reply
  - service-activator
---

# Command Message

## Intent
Represent an instruction to perform work as a message.

## When To Use
- A receiver is expected to take an action.
- The command needs correlation, retry, audit, or scheduling.
- The action can be made idempotent or guarded.

## Avoid When
- The sender is only announcing that something happened.
- The command name is vague or CRUD-shaped without business intent.
- The receiver cannot safely handle retries.
