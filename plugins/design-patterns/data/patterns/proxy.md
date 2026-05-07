---
slug: proxy
name: Proxy
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
  - decorator
  - adapter
  - facade
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Proxy

## Intent
Control access to another object through a stand-in with the same interface.

## When To Use
- Access needs lazy loading, authorization, caching, remoting, or instrumentation.
- The client should not know whether the target is local, remote, or expensive.
- A boundary needs policy without changing the target implementation.

## Avoid When
- The proxy hides network or failure semantics that callers must handle.
- Policy belongs in middleware or infrastructure.
- The proxy violates substitutability.

## Language Notes

### csharp
Dynamic proxies are useful but can obscure behavior; explicit wrappers are easier to test.

### java
Framework proxies are common; be mindful of self-invocation and lifecycle surprises.

### typescript
Use explicit wrappers unless JavaScript Proxy is truly needed.

### python
Descriptors and wrapper objects can proxy access; keep magic limited.

### go
Interface wrappers make proxies simple and explicit.

### rust
Use wrapper types and traits; async proxies should expose failure clearly.

### cpp
Proxy objects should make ownership and latency visible.
