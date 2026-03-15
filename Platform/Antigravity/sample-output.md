# Antigravity Sample Output

## Context and Assumptions

- Project type: Unity game
- Genre: casual
- Multiplayer: lightweight session-based

## Planning Document Domain Map

- `docs/overview.md` -> Account, Progression
- `docs/stage-design.md` -> StageRuntime, GameplaySimulation
- `docs/liveops.md` -> LiveOps, Analytics

## Recommended Structure

- Outgame(DDD): Account, Progression, Economy, LiveOps, Analytics
- Ingame(ECS): StageRuntime, GameplaySimulation
- Multiplayer: Session + Replication behind Port/Adapter

## Next Steps

1. Confirm canonical docs per domain.
2. Generate starter folder tree.
3. Create first implementation batch.
