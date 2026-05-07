---
slug: singleton
name: Singleton
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
  - facade
  - flyweight
---

# Singleton

## Intent
Ensure one logical instance exists and provide controlled access to it.

## When To Use
- A resource is truly unique within a process and must be coordinated.
- The lifecycle is explicit, testable, and safe under concurrency.
- Global access is less harmful than passing the dependency everywhere.

## Avoid When
- The instance is only convenient global mutable state.
- Tests need parallel isolation.
- Dependency injection or explicit ownership would clarify lifecycle.

## Language Notes

### csharp
Prefer DI singleton lifetimes; static singletons should be rare and immutable.

### java
Enums are safe for simple singletons; Spring singletons are often the better lifecycle owner.

### typescript
Module scope already creates single-instance behavior in many runtimes.

### python
Module-level objects are usually clearer than metaclass singletons.

### go
Use package-level state sparingly and guard initialization with sync.Once when needed.

### rust
Use OnceLock or LazyLock for explicit one-time initialization.

### cpp
Use function-local statics carefully and avoid global teardown surprises.
