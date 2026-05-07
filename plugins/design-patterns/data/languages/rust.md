---
slug: rust
displayName: Rust
---

# Rust

## Object Design Idioms
- Prefer traits, enums, pattern matching, ownership boundaries, and zero-cost abstractions.
- Use Strategy with generic trait bounds or trait objects depending on whether runtime dispatch is needed.
- Builder is common for complex configuration; Singleton usually becomes explicit shared state with OnceLock or dependency injection.

## Integration Stacks
- Tokio
- async-nats
- rdkafka
- lapin
- Axum
- Tower
