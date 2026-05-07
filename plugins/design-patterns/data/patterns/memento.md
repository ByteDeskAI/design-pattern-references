---
slug: memento
name: Memento
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
  - command
  - prototype
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Memento

## Intent
Capture an object's state so it can be restored later without exposing internals.

## When To Use
- Undo, rollback, checkpoints, or snapshots are required.
- State capture must preserve encapsulation.
- The snapshot format can remain private to the originator.

## Avoid When
- Snapshots are too large or frequent without compaction.
- State should be event-sourced instead.
- Persistence format stability is required across versions.

## Language Notes

### csharp
Records and immutable snapshots are useful; watch memory pressure.

### java
Immutable mementos work well; do not leak internal mutable collections.

### typescript
Serialize explicit state slices rather than entire object graphs.

### python
Copy only the state needed for restore; avoid deep-copy surprises.

### go
Use explicit snapshot structs and restore methods.

### rust
Ownership makes snapshot boundaries explicit; clone only necessary state.

### cpp
Use value snapshots with clear copy/move cost.
