---
slug: state
name: State
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
  - strategy
  - flyweight
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
---

# State

## Intent
Change an object's behavior when its internal state changes by delegating to state-specific behavior.

## When To Use
- Large conditionals switch behavior by lifecycle state.
- State transitions have rules and side effects worth isolating.
- The set of states is explicit and central to the model.

## Avoid When
- A simple enum and switch is clearer.
- Transitions are not well-defined.
- State classes duplicate most behavior.

## Language Notes

### csharp
Use state objects for complex lifecycles; enums and pattern matching may be enough.

### java
Sealed types can model closed state sets cleanly.

### typescript
Discriminated unions and state machines are often better than class states.

### python
Use explicit transition tables or small state classes.

### go
State functions or small interfaces can avoid ceremony.

### rust
Enums and typestate patterns are powerful options.

### cpp
Use variants or polymorphic states depending on runtime extension needs.
