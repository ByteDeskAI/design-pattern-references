# Pattern Finder Catalog Use

## Useful Queries

```bash
patterns domains
patterns search "factory" --scope object-design
patterns search "router" --scope integration-design
patterns list behavior-and-collaboration --language python
patterns list message-routing
patterns show idempotent-receiver
```

## Shortlist Rules

- Start from the user's force, not from famous pattern names.
- Use `groups` for broad filtering and `domain` for precise filtering.
- Use `related` patterns to find close alternatives.
- Use language profiles to prevent class-heavy recommendations in function-first languages.

## Pattern File Fields

- `groups` tells whether the pattern is object-design or integration-design.
- `domain` tells the more precise design area.
- `related` provides comparison candidates.
- `references` points to skill implementation docs that explain how to use the pattern in practice.

