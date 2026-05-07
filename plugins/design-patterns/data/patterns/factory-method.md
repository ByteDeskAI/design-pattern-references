---
slug: factory-method
name: Factory Method
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
  - template-method
---

# Factory Method

## Intent
Let subclasses or collaborators decide which concrete product to create through a stable creation method.

## When To Use
- A framework or base type needs extension-specific products.
- Creation is a variation point but the client should depend on an abstraction.
- Construction depends on local context in the creator.

## Avoid When
- A direct constructor or small named function is clearer.
- Subclassing exists only to choose a type.
- The method hides important dependency or lifetime choices.

## Language Notes

### csharp
Often appears as virtual factory methods, delegates, or typed factories registered in DI.

### java
Useful in frameworks; static factories are often enough for simpler APIs.

### typescript
Use functions or class static constructors; abstract creators are rarely necessary.

### python
Class methods and callables are natural factory methods.

### go
Use constructor functions; interfaces belong at the consumer side.

### rust
Use associated functions or trait methods when construction varies behind a trait.

### cpp
Use virtual creation carefully and return smart pointers.
