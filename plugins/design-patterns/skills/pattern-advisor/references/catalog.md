# Pattern Advisor Catalog Use

## Primary Commands

```bash
patterns domains
patterns list object-design --language typescript
patterns list integration-design --language csharp
patterns search "router" --scope integration-design
patterns show strategy --language csharp
patterns languages go
```

## Domain Selection

- Use `object-design` when the main force is object construction, structure, collaboration, state, or algorithm variation.
- Use `integration-design` when the main force is messaging, routing, transformation, endpoint behavior, delivery, operations, or cross-system workflow.
- Use a narrower domain when the user names a specific force, such as `message-routing`, `object-construction`, or `operations-and-observability`.

## Reading Pattern Files

Pattern files provide:

- frontmatter for filtering;
- intent for quick fit;
- when-to-use and avoid-when bullets for tradeoffs;
- language notes for object-design patterns;
- reference links to skill documentation.

Prefer direct pattern files over memory when a user asks for a precise catalog-backed recommendation.

