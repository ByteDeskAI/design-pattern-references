---
slug: chain-of-responsibility
name: Chain of Responsibility
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
  - command
  - composite
---

# Chain of Responsibility

## Intent
Pass a request along a chain of handlers until one handles it or the chain completes.

## When To Use
- Multiple handlers may process or reject a request in sequence.
- The sender should not know which handler will respond.
- Handler order is configurable or policy-driven.

## Avoid When
- The chain makes control flow invisible.
- Every request should always be handled by a known component.
- A pipeline or middleware abstraction already exists.

## Language Notes

### csharp
ASP.NET middleware and MediatR behaviors are common chain forms.

### java
Servlet filters, Spring interceptors, and validation chains are familiar forms.

### typescript
Middleware arrays or handler pipelines are idiomatic.

### python
Decorator stacks and middleware chains often cover this.

### go
HTTP middleware and functional chaining are idiomatic.

### rust
Tower services and layers provide a strong chain model.

### cpp
Use explicit handler ownership and avoid null-next ambiguity.
