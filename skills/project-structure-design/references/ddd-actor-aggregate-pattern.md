# DDD Aggregate with Actor Model

Use this reference when aggregate implementation must follow Actor Model.

## Core Mapping

- `Aggregate Type` -> `Actor Kind`
- `Aggregate ID` -> `Actor Identity`
- `Command` -> `Actor Message (command)`
- `Domain Event` -> `Published Event`
- `Aggregate State` -> `Actor State`

## Invariant Rule

- Handle one command at a time per aggregate actor.
- Validate invariants before mutating state.
- Reject invalid command with explicit domain error.
- Persist/apply state transition, then publish domain event.

## Message Types

- Command: intent to change state (`CreateOrder`, `ConfirmPayment`)
- Query: read-only projection request (prefer read model for heavy reads)
- Internal timer/retry message: timeout, compensation, retry

## Suggested Folder Shape

```text
src/
  contexts/
    order/
      domain/
        aggregates/
          order/
            OrderAggregateActor.cs
            OrderCommands.cs
            OrderEvents.cs
            OrderState.cs
            OrderDomainFunctions.cs
      application/
        handlers/
      infrastructure/
        actor/
          OrderActorRuntime.cs
          SnapshotStore.cs
```

## Reliability Checklist

- Is actor identity stable and deterministic from aggregate id?
- Is command processing idempotent where duplicates are possible?
- Is snapshot/replay strategy defined?
- Are poison-message and dead-letter handling rules explicit?
- Are retry/backoff policies bounded and observable?

## Design Guidance

- Keep aggregate logic framework-agnostic; isolate actor runtime details in infrastructure.
- Keep core domain transitions in pure static functions; let actor runtime call them.
- Keep cross-aggregate workflow in process manager/saga, not inside one aggregate.
- Keep transactions local to one aggregate actor; use eventual consistency across aggregates.
