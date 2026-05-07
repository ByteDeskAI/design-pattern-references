---
slug: observer
name: Observer
domain: behavior-and-collaboration
category: Behavior and Collaboration
groups:
  - object-design
languages:
  - csharp
  - java
  - typescript
  - python
  - go
  - rust
  - cpp
related:
  - mediator
  - publish-subscribe-channel
---

# Observer

## Intent
Notify dependents when an object changes without tightly coupling the subject to its observers.

## When To Use
- Multiple dependents react to state changes.
- Publishers should not know concrete subscribers.
- Event ordering and delivery are local and manageable.

## Avoid When
- Observers introduce hidden side effects or ordering dependencies.
- Durable integration messaging is required instead.
- Subscription lifetimes are hard to manage.

## Language Notes

### csharp
Events, IObservable, and channels cover different observer needs.

### java
Use listeners, reactive streams, or event publishers; avoid deprecated Observable.

### typescript
Event emitters, callbacks, RxJS, or signals are common.

### python
Callbacks, signals, and async queues are simple observer forms.

### go
Channels can model local observation but need cancellation and backpressure.

### rust
Use channels or callback registries with clear ownership.

### cpp
Manage subscription lifetimes explicitly to avoid dangling observers.
