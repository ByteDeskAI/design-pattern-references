---
slug: invalid-message-channel
name: Invalid Message Channel
domain: message-channel
category: Messaging Channels
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
  - dead-letter-channel
  - message-filter
  - test-message
---

# Invalid Message Channel

## Intent
Route messages that fail validation to a dedicated channel for inspection or repair.

## When To Use
- Malformed or semantically invalid messages must not block normal flow.
- Operations needs visibility into contract violations.
- Some invalid messages may be corrected and replayed.

## Avoid When
- Invalid data should be rejected synchronously at the producer.
- The channel becomes an unmonitored dumping ground.
- Sensitive payloads would be exposed without controls.
