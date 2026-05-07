---
slug: prototype
name: Prototype
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
  - memento
---

# Prototype

## Intent
Create new objects by copying an existing configured instance.

## When To Use
- Object setup is expensive or mostly repeated.
- Runtime configuration should define new instances.
- The system needs to clone variants without knowing concrete classes.

## Avoid When
- Copy semantics are ambiguous or resource-heavy.
- Shared mutable state could leak between clones.
- A simple factory can reconstruct the object safely.

## Language Notes

### csharp
Use records, copy constructors, or explicit clone methods; avoid ambiguous ICloneable semantics.

### java
Prefer copy constructors or factories over Cloneable unless the behavior is tightly controlled.

### typescript
Use object spread or structured cloning for data; custom clone methods for behavior-rich objects.

### python
Use copy protocols deliberately and document shallow versus deep behavior.

### go
Use explicit Copy methods for structs with slices, maps, or pointers.

### rust
Derive or implement Clone when ownership semantics are clear.

### cpp
Use virtual clone with unique_ptr for polymorphic copies.
