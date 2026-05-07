---
slug: interpreter
name: Interpreter
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
  - composite
  - visitor
---

# Interpreter

## Intent
Represent grammar rules as objects and evaluate sentences in that grammar.

## When To Use
- A small language or expression grammar is central to the domain.
- Rules must be composed, inspected, or transformed.
- A full parser generator would be too heavy.

## Avoid When
- The grammar is complex or performance-sensitive.
- A parser library, rules engine, or query language already fits.
- The object model mirrors syntax but not useful semantics.

## Language Notes

### csharp
Expression trees or parser libraries may be better for non-trivial languages.

### java
Parser combinators or ANTLR often replace hand-built interpreters.

### typescript
Discriminated unions make AST interpretation clear.

### python
Parser libraries and simple AST dataclasses are natural.

### go
Keep grammar structs explicit and small; use parser generators for complexity.

### rust
Enums and pattern matching are excellent for AST interpreters.

### cpp
Use variants or class hierarchies depending on grammar openness.
