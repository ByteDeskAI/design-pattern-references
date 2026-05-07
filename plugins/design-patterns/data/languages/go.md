---
slug: go
displayName: Go
---

# Go

## Object Design Idioms
- Prefer small interfaces at consumers, functions, composition, and explicit construction.
- Many object-design patterns collapse into interfaces plus structs; avoid Java-style inheritance emulation.
- Use channels and context cancellation carefully; they do not replace durable messaging semantics.

## Integration Stacks
- Watermill
- NATS
- Kafka
- RabbitMQ
- Temporal
- gRPC
