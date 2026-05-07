---
slug: decorator
name: Decorator
domain: object-structure
category: Structure
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
  - adapter
  - composite
  - proxy
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Decorator

## Intent
Add responsibilities to an object dynamically by wrapping it with another object that preserves the same interface.

## When To Use
- Behavior must be composed without modifying the original type.
- Cross-cutting behavior should be layered in a controlled order.
- Inheritance would create too many combinations.

## Avoid When
- Order-dependent wrappers make behavior hard to reason about.
- A middleware pipeline or language decorator is the established local idiom.
- The wrapper changes the contract rather than extending behavior.

## Language Notes

### csharp
Use decorators with DI for logging, caching, validation, or policies.

### java
Classic for streams and middleware-like wrappers.

### typescript
Use higher-order functions, wrappers, or framework middleware.

### python
Function decorators and wrapper classes are both natural.

### go
Wrap interfaces explicitly; functions returning functions work for handlers.

### rust
Newtype wrappers and Tower layers are common Decorator-like forms.

### cpp
Prefer composition wrappers and clear ownership.
