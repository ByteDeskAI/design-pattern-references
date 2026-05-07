---
slug: template-method
name: Template Method
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
  - factory-method
  - strategy
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Template Method

## Intent
Define an algorithm skeleton while letting subclasses or hooks customize selected steps.

## When To Use
- Several operations share a fixed sequence with variable steps.
- A framework controls the lifecycle and exposes hook points.
- Invariant ordering must be protected.

## Avoid When
- Inheritance is only being used for configuration.
- Hooks multiply until the algorithm is hard to follow.
- Composition with Strategy would make variation clearer.

## Language Notes

### csharp
Use abstract base classes sparingly; protected virtual hooks can become brittle.

### java
Common in frameworks; prefer final template methods for invariant order.

### typescript
Prefer composition or callbacks unless class inheritance is already idiomatic.

### python
Base classes with overridable hooks work but functions can be simpler.

### go
Use functions and interfaces; inheritance-style templates do not map directly.

### rust
Traits with default methods can express template behavior.

### cpp
Non-virtual interface style can protect algorithm order.
