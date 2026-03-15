# Claude Sample Output

## Context and Assumptions

- Project type: Unity game
- Genre: casual
- Planning depth: medium

## Domain Extraction Summary

- Outgame(DDD): Progression, Economy, LiveOps, Analytics
- Ingame(ECS): StageRuntime, GameplaySimulation

## Architecture Recommendation

- Keep Outgame business logic in bounded contexts.
- Keep Ingame runtime logic in ECS modules.
- Keep multiplayer behind Port/Adapter boundaries.

## Next Steps

1. Confirm progression and economy assumptions.
2. Generate starter folder tree.
3. Define first migration or implementation batch.
