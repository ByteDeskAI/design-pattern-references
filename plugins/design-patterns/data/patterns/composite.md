---
slug: composite
name: Composite
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
  - iterator
  - visitor
  - decorator
---

# Composite

## Intent
Represent part-whole hierarchies so clients can treat individual objects and groups uniformly.

## When To Use
- The domain naturally forms trees or nested structures.
- Operations should apply recursively across leaves and groups.
- Client code should not branch on leaf versus container for every operation.

## Avoid When
- The hierarchy is shallow and explicit handling is clearer.
- Parent-child ownership or mutation rules are hard to enforce.
- Uniform treatment hides important differences between leaves and groups.

## Language Notes

### csharp
Use interfaces plus immutable collections when possible; expose mutation carefully.

### java
Works well with sealed interfaces for closed hierarchies.

### typescript
Discriminated unions can model composites without class inheritance.

### python
Simple protocols and recursive dataclasses are often enough.

### go
Use interfaces and slices for children; avoid deep inheritance-style APIs.

### rust
Enums are excellent for closed composite trees; traits fit open hierarchies.

### cpp
Use smart pointers or value trees with explicit ownership.
