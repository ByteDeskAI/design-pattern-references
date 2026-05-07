---
slug: bridge
name: Bridge
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
  - strategy
  - abstract-factory
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Bridge

## Intent
Separate an abstraction from its implementation so both can vary independently.

## When To Use
- Two dimensions of variation are being forced into one inheritance tree.
- A stable API must support multiple providers, platforms, or renderers.
- Implementation details should be swappable without changing client code.

## Avoid When
- There is only one dimension of variation.
- A simple strategy or dependency interface is clearer.
- The abstraction mirrors the implementation too closely.

## Language Notes

### csharp
Use interfaces for implementors and keep abstraction responsibilities meaningful.

### java
Good for provider-backed APIs; avoid creating parallel hierarchies without real variation.

### typescript
Use composition with typed provider contracts.

### python
Composition and protocols are usually enough.

### go
Consumer-owned interfaces often express the bridge naturally.

### rust
Use traits and generic parameters for static bridges or trait objects for runtime switching.

### cpp
The pimpl idiom is a common Bridge-like technique for ABI stability.
