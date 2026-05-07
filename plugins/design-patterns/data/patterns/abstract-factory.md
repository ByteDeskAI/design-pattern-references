---
slug: abstract-factory
name: Abstract Factory
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
  - factory-method
  - builder
  - prototype
---

# Abstract Factory

## Intent
Create related families of objects through stable interfaces without binding clients to concrete product classes.

## When To Use
- A caller must create several compatible objects that vary as a family.
- Product families change by platform, tenant, theme, provider, or environment.
- Construction policy belongs at a boundary rather than in domain logic.

## Avoid When
- Only one object varies; Factory Method or a simple factory is enough.
- A dependency injection container already owns the variation cleanly.
- The factory hierarchy is larger than the product hierarchy.

## Language Notes

### csharp
Use interfaces plus DI registrations or factory delegates; keep the factory itself small and testable.

### java
Works well with interfaces and provider modules; avoid duplicating Spring configuration in factory classes.

### typescript
Prefer typed object factories or provider maps over abstract class trees.

### python
Use protocols or callable factories; module-level factories are often sufficient.

### go
Return interfaces from explicit constructor functions only when the caller benefits from abstraction.

### rust
Use traits and associated factory functions; generics may remove the need for runtime factories.

### cpp
Use abstract product interfaces with smart pointers and clear ownership.
