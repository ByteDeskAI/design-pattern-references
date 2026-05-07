---
slug: strategy
name: Strategy
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
  - state
  - command
  - template-method
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Strategy

## Intent
Define interchangeable algorithms behind a common contract.

## When To Use
- A behavior varies independently from the object that uses it.
- Callers need runtime or configuration-driven algorithm selection.
- Conditionals select among algorithms with the same input and output shape.

## Avoid When
- There are only one or two trivial branches.
- Strategies require access to too much host object state.
- A simple function parameter communicates the variation better.

## Language Notes

### csharp
Use interfaces, delegates, or keyed services depending on selection needs.

### java
Functional interfaces and lambdas are lightweight strategy forms.

### typescript
Function maps and typed callbacks are usually ideal.

### python
Callables are often the cleanest strategy.

### go
Interfaces or function types both work; keep contracts tiny.

### rust
Use generics for static dispatch or trait objects for runtime selection.

### cpp
Use templates, function objects, or polymorphism based on binding needs.
