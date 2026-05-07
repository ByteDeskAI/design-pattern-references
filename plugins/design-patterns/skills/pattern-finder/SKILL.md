---
description: Use when the user describes a design problem and wants help finding, comparing, or choosing GoF or Enterprise Integration Patterns.
---

# Pattern Finder

Use this skill to turn a problem statement into a short, practical pattern shortlist.

Start by identifying the forces in the user's request:

- Source of variation: object creation, algorithm choice, object structure, lifecycle state, collaboration, message routing, transformation, delivery, or operations.
- Coupling pressure: which components know too much about each other.
- Runtime pressure: latency, durability, ordering, throughput, retries, observability, or deployment independence.
- Change pressure: what is likely to vary next.
- Language and framework: whether the local stack already has an idiom that should be preferred.

Lookup workflow:

1. Run `patterns search "$ARGUMENTS"` when the user names a pattern, force, or term.
2. Run `patterns list gof` for object design problems or `patterns list eip` for messaging and integration problems.
3. Read the relevant `data/*.json` entries before making a recommendation.

Response shape:

1. State the likely primary pattern.
2. Give two close alternatives and why they are weaker or stronger.
3. Explain what code or architecture would change.
4. Include language-specific advice if the language is known.
5. Name the signals that would make you change the recommendation.

Keep the shortlist tight. A good recommendation is usually one pattern, one backup, and one "do not use a pattern yet" option.

