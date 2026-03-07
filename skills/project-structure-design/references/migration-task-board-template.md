# Migration Task Board Template

Use this document to manage migration scope and progress.

## Status Definition

- `Planned`: identified but not yet actionable
- `Ready`: preconditions satisfied, executable now
- `InProgress`: currently being executed
- `Verify`: implementation done, waiting for gate checks
- `Done`: validated and merged
- `Blocked`: cannot proceed due to dependency

## Engine Migration Fields

- `Disposition`: `retain`, `wrap`, `replace`, `defer`, or `drop`
- `Source of Truth`: `legacy engine`, `new engine`, `shared neutral format`, or `manual sync`
- `Cutover Mode`: `side-by-side`, `shadow/dual-run`, `slice-by-slice`, or `big-bang`
- `Parity Gate`: the concrete proof required before ownership or traffic moves
- Use these fields whenever runtime, engine, or asset pipeline migration is in scope.

## Task Board

```markdown
| Task ID | Domain/Slice | Scope | Disposition | Source of Truth | Cutover Mode | Parity Gate | Preconditions | Status | Owner | Risk | Rollback | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIG-001 | Save/Load | Extract save format adapter | wrap | shared neutral format | shadow/dual-run | old/new save files round-trip with identical gameplay state | neutral schema agreed | Ready | @owner | Medium | route writes to legacy serializer | test-report-link |
| MIG-002 | Scene Flow | Move level loading to new runtime | replace | new engine | slice-by-slice | target level boots within load budget and event parity checklist passes | MIG-001 done | Planned | @owner | High | route affected scene to legacy launcher | dashboard-link |
```

## Task Detail Template

```markdown
### MIG-001 - Extract read model adapter

- Objective:
- Scope in:
- Scope out:
- Dependencies:
- Disposition:
- Source of Truth:
- Cutover Mode:
- Parity Gate:
- Execution steps:
1.
2.
3.
- Validation gate:
  - Unit/Integration:
  - Performance:
  - Observability:
- Rollback plan:
- Result notes:
```

## Batch Plan

Track execution in small batches:

```markdown
## Batch 01
- Included tasks: MIG-001, MIG-003
- Expected window:
- Go/No-Go criteria:
- Post-check:
```

## Governance Rules

- Do not execute `Planned` tasks.
- Do not close tasks without evidence links.
- Do not merge batches without rollback strategy.
- Re-estimate and split tasks when scope exceeds 2 days.

## Operational Limits (Recommended Defaults)

- WIP limit per owner: max 2 `InProgress` tasks.
- Batch size: 2-5 tasks per batch.
- Blocked SLA: escalate if `Blocked` state exceeds 1 business day.
- Verify SLA: complete gate checks within 1 business day after `Verify`.

## Gate Ownership Rules

- Assign a gate owner per task (`quality owner`).
- Assign rollback owner per task (`rollback owner`).
- Task cannot move to `Done` without explicit gate owner sign-off.

## Definition of Done (DoD)

A task is `Done` only when all are true:
- implementation merged
- validation gates are green
- parity gate is met and evidence is recorded
- observability evidence link is recorded
- rollback note is updated
- affected docs/ADRs are updated

## Weekly Board Review

- Review blocked tasks and dependency chain.
- Drop stale tasks with no executable path.
- Re-scope overgrown tasks into smaller reversible units.
