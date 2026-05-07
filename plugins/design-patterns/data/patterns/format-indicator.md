---
slug: format-indicator
name: Format Indicator
domain: message-construction
category: Message Construction
groups:
  - integration-design
languages:
  - csharp
  - java
  - typescript
  - python
  - go
  - rust
  - cpp
related:
  - datatype-channel
  - message-translator
  - normalizer
references:
  - skills/pattern-advisor/references/implementation.md
  - skills/pattern-finder/references/implementation.md
  - skills/pattern-application/references/implementation.md
  - skills/architecture-issue-scan/references/implementation.md
  - skills/integration-flow-review/references/implementation.md
---

# Format Indicator

## Intent
Include metadata that identifies the payload format or version.

## When To Use
- Multiple schema versions or encodings may coexist.
- Consumers need safe dispatch to the right parser.
- Schema migration needs explicit compatibility signals.

## Avoid When
- The channel already guarantees a single schema.
- Consumers ignore the indicator and guess anyway.
- Version policy is not documented.
