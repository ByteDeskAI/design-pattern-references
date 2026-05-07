---
description: Use when designing or reviewing message-driven, event-driven, async workflow, broker, queue, stream, saga, or enterprise integration architecture.
---

# Integration Flow Review

Use this skill for Enterprise Integration Patterns and message-driven architecture.

Start by mapping the flow:

- Producers, consumers, and ownership boundaries.
- Message type: command, document, event, request-reply, or sequence.
- Channel type: point-to-point, publish-subscribe, datatype, invalid, dead-letter, or bridge.
- Routing and transformation: filters, content-based routers, recipient lists, splitters, aggregators, normalizers, translators, or claim checks.
- Endpoint behavior: polling, event-driven, competing consumers, selective consumers, idempotent receivers, or service activators.
- Operations: correlation identifiers, message history, wire taps, message stores, test messages, and purging.

Review forces:

- Delivery semantics and duplicate handling.
- Ordering, partitioning, and resequencing.
- Backpressure, retries, timeouts, and terminal failure.
- Payload size, schema versioning, and privacy.
- Observability, audit, replay, and support tooling.
- Consumer autonomy and producer coupling.

Lookup workflow:

1. Use `patterns list eip` to survey the catalog.
2. Use `patterns show <slug>` for candidate EIP entries.
3. Use `data/languages.json` for ecosystem-specific implementation options.

Output should include:

1. Flow summary in the user's terms.
2. Recommended EIP pattern set.
3. Failure-mode checklist.
4. Concrete implementation sketch for the user's stack.
5. Observability and operations hooks.

Prefer a small pattern set. Most flows need a channel, a message construction choice, one routing or transformation choice, one endpoint pattern, and explicit operations patterns.

