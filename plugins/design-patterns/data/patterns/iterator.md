---
slug: iterator
name: Iterator
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
  - composite
  - visitor
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Iterator

## Intent
Provide sequential access to elements without exposing the underlying representation.

## When To Use
- Clients need traversal without knowing collection internals.
- Different traversal orders should be supported.
- Traversal state must be externalized or composable.

## Avoid When
- The language's native iteration protocol is enough.
- Exposing iteration hides expensive remote or streaming behavior.
- A query abstraction communicates intent better.

## Language Notes

### csharp
Use IEnumerable, yield return, and async streams.

### java
Use Iterable, streams, or spliterators as appropriate.

### typescript
Use iterable protocols, generators, and async iterables.

### python
Use iterators, generators, and context-aware streaming.

### go
Range works for built-ins; iterator functions are emerging idioms.

### rust
Iterator is a central trait; compose adapters freely.

### cpp
STL iterators and ranges are the idiomatic form.
