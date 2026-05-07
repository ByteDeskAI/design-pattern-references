---
slug: mediator
name: Mediator
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
  - facade
  - observer
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Mediator

## Intent
Centralize complex collaboration so peers do not reference each other directly.

## When To Use
- Many components have tangled peer-to-peer interactions.
- Coordination rules should be explicit and testable.
- A workflow or UI interaction needs a single orchestration point.

## Avoid When
- The mediator becomes a god object.
- Direct events or domain services would be clearer.
- The central coordinator hides ownership of business rules.

## Language Notes

### csharp
MediatR-style dispatch is useful; avoid replacing every method call with mediation.

### java
Application services or event buses often act as mediators.

### typescript
State machines or event buses can mediate UI and workflow interactions.

### python
Simple coordinator objects are usually enough.

### go
Prefer explicit orchestration functions unless decoupling is valuable.

### rust
Use coordinators with explicit ownership and message passing when concurrency is involved.

### cpp
Mediator can simplify UI object graphs but needs tight responsibility control.
