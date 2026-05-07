---
slug: file-transfer
name: File Transfer
domain: integration-style
category: Integration Styles
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
  - message
  - channel-adapter
---

# File Transfer

## Intent
Exchange data by writing and reading files through a shared transfer location.

## When To Use
- Batch delivery is acceptable.
- Participants cannot share a live API or message broker.
- Operational teams already manage file drops, checksums, and retention.

## Avoid When
- Low latency or fine-grained feedback is required.
- Partial files and duplicate processing cannot be controlled.
- Schema evolution is unmanaged.
