---
slug: command
name: Command
domain: behavior-and-collaboration
category: Behavior and Collaboration
groups:
  - object-design
languages:
  - csharp
  - java
  - typescript
  - python
  - go
  - rust
  - cpp
related:
  - memento
  - strategy
  - request-reply
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Command

## Intent
Encapsulate a request as an object so it can be queued, logged, retried, undone, or passed around.

## When To Use
- Requests need durable handling, scheduling, retries, audit, or undo.
- The invoker should be decoupled from the receiver.
- Operations need consistent metadata and lifecycle.

## Avoid When
- A direct function call is sufficient.
- Command objects become anemic wrappers around one method call.
- The command hides transactional boundaries.

## Language Notes

### csharp
Commands pair well with CQRS/MediatR but should carry clear intent and validation.

### java
Use command handlers or functional interfaces depending on ceremony needs.

### typescript
Plain objects plus handler maps often beat class hierarchies.

### python
Dataclasses plus handler functions are clean command representations.

### go
Struct commands plus explicit handlers keep flow visible.

### rust
Enums are strong for closed command sets; traits fit open extension.

### cpp
Use callable objects or command classes depending on undo/lifetime needs.
