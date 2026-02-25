# Sample Report (Casual Game)

## Core Priorities

- short session loop
- stage content throughput
- retention/live-ops iteration speed

## Domain Split

- Outgame(DDD): Account, Progression, Economy, LiveOps, Analytics
- Ingame(ECS): StageRuntime, GameplaySimulation

## Quality Notes

- Analytics domain is first-class for tuning and A/B loops.
- Economy remains simple but observable from day one.

## Suggested Tree

See `sample-folder-tree.txt`.
