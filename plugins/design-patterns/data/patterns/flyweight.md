---
slug: flyweight
name: Flyweight
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
  - composite
  - singleton
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Flyweight

## Intent
Share fine-grained immutable state to support large numbers of similar objects efficiently.

## When To Use
- Many objects repeat substantial intrinsic state.
- Memory pressure is material and measurable.
- Extrinsic state can be supplied by the caller or context.

## Avoid When
- Sharing introduces hidden mutation or lifecycle coupling.
- The memory savings are speculative.
- Caching policy is more important than object identity.

## Language Notes

### csharp
Use interned values, immutable records, or caches with clear eviction policy.

### java
Value objects, enums, and caches often cover Flyweight needs.

### typescript
Use shared immutable objects or maps; beware accidental mutation.

### python
Interning, slots, and cached immutable values can help.

### go
Use shared immutable structs or lookup tables.

### rust
Arc plus immutable data or interning crates can express shared state.

### cpp
Use shared immutable data and profile allocation behavior.
