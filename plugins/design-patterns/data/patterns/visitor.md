---
slug: visitor
name: Visitor
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
  - interpreter
  - iterator
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Visitor

## Intent
Represent operations over an object structure separately from the classes in that structure.

## When To Use
- A stable object structure needs many operations added over time.
- Operations need type-specific behavior across a hierarchy.
- You want to keep traversal separate from operation logic.

## Avoid When
- The object structure changes frequently.
- Pattern matching or multimethods are clearer in the language.
- Visitors become large switchboards with poor cohesion.

## Language Notes

### csharp
Pattern matching and discriminated-union libraries may replace classic visitors.

### java
Useful for ASTs; sealed classes and pattern matching reduce ceremony.

### typescript
Discriminated unions plus switch exhaustiveness often beat visitor classes.

### python
functools.singledispatch can be a lightweight visitor alternative.

### go
Use explicit type switches or visitor interfaces for stable trees.

### rust
Pattern matching over enums is usually the first choice.

### cpp
std::variant with visitors is idiomatic for closed sets; classic visitors fit open operations.
