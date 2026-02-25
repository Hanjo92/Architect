# Game Architecture Split: Outgame DDD, Ingame ECS

Use this reference only when the project is a game.

## Mandatory Split

- Outgame: apply Domain-Driven Design.
- Ingame: apply Entity-Component-System.

## Outgame Scope (DDD)

Typical domains:
- account/profile
- progression/quest/reward
- inventory/shop/currency
- matchmaking/lobby/social
- live-ops/event/pass

Model as bounded contexts and aggregates.
Use actor-based aggregate handling when concurrency or contention is high.

## Ingame Scope (ECS)

Typical runtime loop:
- entities: identifiers only
- components: plain data
- systems: pure-ish transforms over component sets

Guidance:
- Keep systems independent and deterministic per tick as much as possible.
- Keep frame-critical logic in ECS; avoid aggregate orchestration in hot path.

## Boundary Contract

Integrate Outgame and Ingame through explicit contracts:
- Outgame -> Ingame: loadout, progression bonuses, unlock state, session config
- Ingame -> Outgame: match result, rewards claim event, telemetry summary

Use event/message contracts with versioning.
Do not share mutable domain models directly across boundaries.

## Suggested Folder Shape

```text
src/
  outgame/
    contexts/
      progression/
      economy/
      social/
  ingame/
    ecs/
      entities/
      components/
      systems/
      pipelines/
  contracts/
    outgame-ingame/
```

## Decision Checklist

- Are Outgame and Ingame ownership boundaries explicit?
- Are Outgame rules isolated from frame-tick ECS systems?
- Are ECS systems free from business-domain side effects?
- Are cross-boundary events versioned and backward-compatible?
