# Migration Task Board Template

Use this document to manage migration scope and progress.

## Status Definition

- `Planned`: identified but not yet actionable
- `Ready`: preconditions satisfied, executable now
- `InProgress`: currently being executed
- `Verify`: implementation done, waiting for gate checks
- `Done`: validated and merged
- `Blocked`: cannot proceed due to dependency

## Task Board

```markdown
| Task ID | Domain/Slice | Scope | Preconditions | Status | Owner | Risk | Rollback | Evidence |
|---|---|---|---|---|---|---|---|---|
| MIG-001 | Progression | Extract read model adapter | Contract v2 published | Ready | @owner | Medium | feature flag off | test-report-link |
| MIG-002 | Economy | Move command path to new context | MIG-001 done | Planned | @owner | High | route to legacy | dashboard-link |
```

## Task Detail Template

```markdown
### MIG-001 - Extract read model adapter

- Objective:
- Scope in:
- Scope out:
- Dependencies:
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
