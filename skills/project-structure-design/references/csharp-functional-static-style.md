# C# Functional Style with Static Class/Functions

Use this reference when implementation must feel like FP in C#.

## Principles

- Favor immutable `record` for state and value objects.
- Implement domain behavior as pure `static` functions.
- Make inputs/outputs explicit; avoid hidden mutable state.
- Push IO, time, random, and network to ports/adapters.

## Recommended Shape

```text
src/
  contexts/
    order/
      domain/
        OrderState.cs
        OrderCommands.cs
        OrderEvents.cs
        OrderErrors.cs
        OrderFunctions.cs
      application/
        OrderService.cs
      infrastructure/
        repositories/
        actor/
```

## Static Function Pattern

- `Validate(state, command) -> DomainError?`
- `Decide(state, command) -> DomainEvent[]`
- `Evolve(state, event) -> State`
- `Handle(state, command) -> Result<(State NewState, DomainEvent[] Events), DomainError>`

## Actor Integration Pattern

- Actor mailbox receives command.
- Actor calls `OrderFunctions.Handle(currentState, command)`.
- On success: persist new state, publish events, update in-memory state.
- On failure: return domain error without state mutation.

## Guardrails

- Do not place business rules in instance methods with hidden fields.
- Do not mutate collections in domain layer; create new values.
- Do not call infrastructure directly from domain functions.
- Keep composition simple: small functions over deep inheritance.

## Naming Convention (Clean Code)

- Use intention-revealing names; avoid vague names like `Data`, `Manager`, `Util`, `Temp`.
- Use PascalCase for type/member names and camelCase for local variables/parameters.
- Use verb-first names for functions (`CalculateReward`, `ValidateCommand`, `ApplyEvent`).
- Use domain language for aggregates/events/errors (`OrderPlaced`, `PaymentRejected`).
- Keep boolean names readable (`isConnected`, `hasPermission`, `canRetry`).

## Function Summary Rule

- Add XML summary comments to every non-trivial public function.
- Explain intent and business meaning, not line-by-line mechanics.
- Keep summary short (1-2 lines), add `<param>` and `<returns>` when useful.

Example:

```csharp
/// <summary>
/// Validate command against current aggregate state and return a domain error when invariant is broken.
/// </summary>
public static DomainError? Validate(OrderState state, OrderCommand command)
{
    // ...
}
```
