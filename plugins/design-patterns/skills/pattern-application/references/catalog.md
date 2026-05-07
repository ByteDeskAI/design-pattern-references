# Pattern Application Catalog Use

## Lookup Workflow

```bash
patterns show strategy --language typescript
patterns show adapter --language csharp
patterns show idempotent-receiver
patterns search "duplicate" --scope integration-design
patterns languages rust
```

## Applying Catalog Fields

- Use `intent` as the refactor thesis.
- Use `whenToUse` as evidence that the pattern fits.
- Use `avoidWhen` as a pre-implementation safety check.
- Use `languageNotes` to pick idiomatic implementation shape.
- Use `related` to identify alternatives before committing to a design.
- Use `references` to load deeper skill-specific implementation guidance.

## Minimum Implementation Bar

A pattern application should produce:

- clearer ownership;
- reduced branching or coupling;
- testable seams;
- preserved behavior;
- explicit failure handling for integration patterns.

