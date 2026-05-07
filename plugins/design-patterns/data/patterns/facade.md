---
slug: facade
name: Facade
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
  - adapter
  - mediator
  - singleton
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# Facade

## Intent
Provide a simpler interface over a subsystem.

## When To Use
- Callers need a stable, task-oriented API over many moving parts.
- A subsystem should expose fewer dependencies to the rest of the codebase.
- You need a boundary for orchestration, integration, or migration.

## Avoid When
- The facade becomes a large service object with unrelated responsibilities.
- It hides essential domain concepts.
- It duplicates an existing framework boundary.

## Language Notes

### csharp
Application services often serve as facades; keep orchestration separate from domain rules.

### java
Use facade services at module boundaries; do not turn them into transaction-script catchalls.

### typescript
Boundary modules or service classes can present facade APIs.

### python
Module-level functions can be a clean facade.

### go
Package APIs often act as facades over internal implementation.

### rust
Crate public APIs can facade private modules.

### cpp
Facade headers can protect clients from subsystem churn.
