---
slug: adapter
name: Adapter
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
  - bridge
  - facade
  - decorator
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Adapter

## Intent
Convert one interface into another interface expected by a client.

## When To Use
- A useful type or external service has the wrong shape for the local model.
- You need an anti-corruption boundary around vendor or legacy code.
- A migration needs old and new APIs to coexist.

## Avoid When
- The client can depend on the existing interface directly.
- The adapter becomes a dumping ground for unrelated translation rules.
- Data mapping should instead live in a dedicated mapper or translator.

## Language Notes

### csharp
Use adapter classes at infrastructure boundaries; extension methods can help but should not hide IO.

### java
Common around legacy APIs and SDKs; keep adapters free of business decisions.

### typescript
Boundary modules and typed wrapper functions are usually enough.

### python
Thin wrapper objects or functions work well with duck typing.

### go
Small interfaces make adapters very lightweight.

### rust
Use newtype wrappers or trait implementations to adapt behavior.

### cpp
Use composition adapters; multiple inheritance adapters require care.
