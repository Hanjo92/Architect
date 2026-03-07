# Sample Report (Genre-Agnostic Game)

## 1) Context and Assumptions

- Project type: game
- Genre: unspecified (baseline)
- Platform: Unity target assumed
- Multiplayer: optional, prepared by Port/Adapter

## 2) Planning Augmentation Summary

- `Assumed`: basic progression loop exists
- `Proposed`: economy source/sink model
- `Proposed`: social/live features staged after core loop

## 3) Domain Extraction Summary

- Outgame(DDD): Account, Progression, Economy, Social
- Ingame(ECS): GameplaySimulation, CombatRuntime
- Cross-cutting: Contracts, Observability

## 4) Domain Extraction Quality

| Domain | Confidence | Evidence | Open Questions |
|---|---:|---|---|
| Account | 0.80 | planning/account-notes.md | auth provider selection |
| Progression | 0.78 | planning/progression.md | reset policy |
| Economy | 0.74 | planning/economy.md | premium/soft currency split |
| GameplaySimulation | 0.82 | planning/core-loop.md | authoritative tick model |

## 5) Game Split Rules

- Outgame -> DDD bounded contexts
- Ingame -> ECS runtime modules
- Contracts only across boundaries

## 6) Unity UPM Plan

- `com.company.game.foundation`
- `com.company.game.ads`
- `com.company.game.achievements`
- `com.company.game.social`

## 7) Suggested Folder Tree

See `sample-folder-tree.txt`.

## 8) Validation Summary

- Base validator: pass
- Integrity validator: pass

## 9) Optional Migration Scaffold

- `docs/migration/subsystem-classification.md`
- `docs/migration/ambiguity-register.md`
- `docs/migration/task-board.md`
- create compatibility adapters and cutover boundaries when subsystem migration is expected
