# Migration Playbook

Use this playbook when a project must move from current structure to target architecture.

## 0) Create Migration Task Board (Mandatory for large projects)

For medium/large projects, do not run migration as a single activity.
Create a task board document first using [migration-task-board-template.md](migration-task-board-template.md).

Rules:
- every migration action must map to one task id
- execute only tasks marked `Ready`
- update status/checkpoints after each task
- keep rollback notes and evidence links per task
- enforce task board operational limits (WIP, batch size, blocked SLA)

## 1) Baseline Current State

- Inventory current modules, dependencies, ownership, and deployment units.
- Mark high-risk hotspots: tightly coupled domains, shared mutable state, fragile release paths.
- Freeze critical interfaces before major moves.
- Register baseline findings as tasks in the board.

## 2) Define Target and Transition Boundary

- Define target folder structure and dependency direction.
- Define temporary compatibility boundary (ACL/adapters/facade) between old and new areas.
- Decide migration unit: by bounded context, by feature slice, or by runtime component.
- Convert each migration unit into independently deployable task groups.

## 2.5) Classify Shared Subsystems (Mandatory for subsystem-heavy migration)

- Inventory rendering, physics, input, animation, UI, scene/level flow, asset pipeline, save/load, networking, build tooling, editor tooling, backend contracts, analytics, authentication/session, and content pipelines.
- Assign one `Disposition` per subsystem: `retain`, `wrap`, `replace`, `defer`, or `drop`.
- Assign one `Source of Truth` during transition: `legacy engine`, `new engine`, `shared neutral format`, or `manual sync`.
- Assign one `Cutover Mode`: `side-by-side`, `shadow/dual-run`, `slice-by-slice`, or `big-bang`.
- Define one `Parity Gate` per subsystem: behavior parity, content parity, performance budget, determinism, or operational readiness.
- Register unresolved cases in an `Ambiguity Register` with owner, current assumption, missing evidence, and re-evaluation trigger.

## 3) Strangler Rollout Strategy

- Start with one low-risk vertical slice.
- Route only selected flows to new module; keep the rest on legacy path.
- Expand routing slice-by-slice after stability checks.
- Move task status as `Planned -> Ready -> InProgress -> Verify -> Done`.

## 4) Data and Contract Migration

- Version contracts before moving producers/consumers.
- Add backward-compatible mappers during dual-run period.
- Migrate read paths first, then command/write paths.
- Track producer/consumer cutover tasks separately to avoid hidden coupling.

## 5) Runtime Safety and Rollback

- Use feature flags for traffic switching.
- Keep rollback switch for every migration step.
- Define rollback criteria: error rate, latency, consistency breach.
- Require rollback owner and rollback runbook link per task.

## 6) Test and Observability Gate

- Add regression tests for old and new paths.
- Add migration-specific telemetry dashboards and alerts.
- Require green gate on functional, integration, and performance checks.
- Store gate evidence (test report, dashboard link) in task board.

## 7) Decommission Legacy

- Remove dead adapters and legacy routes only after steady-state verification.
- Archive ADRs and migration logs for future reference.
- Re-run architecture checklist after cleanup.
- Close related tasks only after decommission verification.

## Recommended Task Granularity

- Keep each task to 0.5-2 days of effort.
- Split work by reversible boundary: contract, adapter, routing, data sync, cleanup.
- Avoid cross-context mega tasks.

## Execution Loop

Repeat per task batch:
1. Select tasks in `Ready`.
2. Execute smallest safe batch.
3. Run gates and record evidence.
4. Promote to `Done` or rollback to previous state.
5. Replan next batch from board.

## Board Health Gate

Before each batch starts:
- WIP limit is not exceeded.
- No high-priority `Blocked` task exceeds SLA.
- Gate owners are assigned for every `Ready` task.
- DoD checklist is attached for every `Ready` task.

## Deliverable Checklist

- current-vs-target map
- phased migration plan (phase/deliverable/risk/rollback)
- subsystem classification matrix with `Disposition`, `Source of Truth`, `Cutover Mode`, and `Parity Gate` when migration changes shared technical boundaries
- ambiguity register for unresolved subsystem/runtime decisions
- contract versioning plan
- test + observability gate plan
- migration task board with status, owner, checkpoints, evidence, rollback notes
