# Sample Report (RPG Game)

## Core Priorities

- deep progression and build diversity
- inventory/equipment consistency
- quest and world-state integrity

## Domain Split

- Outgame(DDD): Account, Progression, Inventory, Equipment, Quest, Economy, GuildSocial, LiveOps
- Ingame(ECS): CombatRuntime, WorldSimulation, AIRuntime

## Quality Notes

- Inventory/Equipment/Quest boundaries need strict invariant definition.
- Combat and world systems remain ECS-driven for runtime performance.

## Suggested Tree

See `sample-folder-tree.txt`.
