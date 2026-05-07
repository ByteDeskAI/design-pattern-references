# Architecture Issue Scan Catalog Use

## Lookup Commands

```bash
patterns search "strategy" --scope object-design
patterns search "dead letter" --scope integration-design
patterns list operations-and-observability
patterns show adapter --language go
patterns show idempotent-receiver
```

## Finding-to-Domain Map

- repeated behavior branches -> `behavior-and-collaboration`;
- vendor coupling -> `object-structure`;
- tangled construction -> `object-construction`;
- async route decisions -> `message-routing`;
- schema conversion -> `message-transformation`;
- retry and duplicates -> `message-endpoint`;
- trace, replay, and support gaps -> `operations-and-observability`.

## Evidence Standards

Use catalog entries to support findings, but ground every finding in observed code, docs, or runtime behavior. If no evidence exists, report the item as a question or risk hypothesis.

