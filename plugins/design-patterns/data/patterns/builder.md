---
slug: builder
name: Builder
domain: object-construction
category: Construction
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
  - abstract-factory
  - composite
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Builder

## Intent
Separate the construction of a complex object from the representation that is produced.

## When To Use
- Construction has many optional parts, validation steps, or ordering constraints.
- The same assembly process should produce different representations.
- A readable construction DSL would reduce call-site noise.

## Avoid When
- The target object has only a few obvious constructor parameters.
- The builder allows invalid intermediate states to leak.
- Named arguments or records already solve the readability problem.

## Language Notes

### csharp
Records, optional parameters, and object initializers may be enough; use Builder for validation-heavy flows.

### java
Common for immutable objects; consider records for simple data carriers.

### typescript
Prefer typed config objects for simple cases; use fluent builders when staged validation matters.

### python
Dataclasses and keyword arguments usually cover simple cases; use builders for staged workflows.

### go
Functional options are often the idiomatic Builder variant.

### rust
Builder is common for complex structs; encode required fields through types when worth it.

### cpp
Use fluent builders or parameter objects while preserving move semantics.
