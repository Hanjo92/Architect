# Subsystem Migration Decision Matrix

Use this matrix when a project is migrating between engines, major runtime versions, backend/network stacks, asset pipelines, or other shared technical subsystems.

## Goal

- classify ambiguous subsystems before roadmap or folder design
- make cutover ownership explicit
- prevent mixed-runtime migrations from hiding irreversible decisions

## Required Fields Per Subsystem

- `Disposition`: `retain`, `wrap`, `replace`, `defer`, or `drop`
- `Source of Truth`: `legacy engine`, `new engine`, `shared neutral format`, or `manual sync`
- `Cutover Mode`: `side-by-side`, `shadow/dual-run`, `slice-by-slice`, or `big-bang`
- `Parity Gate`: the concrete proof required before cutover
- `Rollback`: the mechanism that restores previous ownership

## Disposition Rules

- `retain`: keep current implementation temporarily because replacement is not yet justified or is too risky
- `wrap`: isolate legacy engine dependency behind a narrow adapter while other systems move forward
- `replace`: build the target subsystem natively in the new engine/runtime
- `defer`: postpone migration until dependent systems or content pipelines are stable
- `drop`: remove subsystem entirely because it is obsolete or not worth carrying forward

## Cutover Mode Rules

- `side-by-side`: old and new implementations exist, but only one owns production traffic/content at a time
- `shadow/dual-run`: both implementations run for comparison; one remains authoritative
- `slice-by-slice`: ownership moves per feature, map, content set, or gameplay loop slice
- `big-bang`: switch all at once only when dependency isolation and rollback are proven

## Suggested Classification Heuristics

| Subsystem | Default Disposition | Common Source of Truth | Recommended Cutover Mode | Example Parity Gate |
|---|---|---|---|---|
| Rendering | replace | new engine | slice-by-slice | visual checklist + frame budget on target hardware |
| Physics | replace | new engine | shadow/dual-run or slice-by-slice | collision outcomes and determinism tolerance within agreed range |
| Input | wrap | legacy engine or shared neutral format | side-by-side | action mapping parity for target devices |
| Animation | wrap or replace | new engine | slice-by-slice | state transition parity for critical gameplay states |
| UI/HUD | replace | new engine | slice-by-slice | interaction flow parity and localization pass |
| Scene/Level Flow | wrap or replace | new engine | slice-by-slice | scene bootstrap, event wiring, and load time budget pass |
| Asset Pipeline | defer or replace | shared neutral format | side-by-side | import/export reproducibility and content validation pass |
| Save/Load | wrap | shared neutral format | shadow/dual-run | old/new save round-trip produces equivalent gameplay state |
| Networking | wrap or replace | legacy engine or new engine | side-by-side | session lifecycle parity and rollback path proven |
| Build/Editor Tooling | defer | legacy engine | side-by-side | developer workflow remains operable during migration |
| Backend Contracts | wrap or replace | shared neutral format | shadow/dual-run or slice-by-slice | v1/v2 contract parity for required user journeys |
| Authentication/Session | wrap or replace | legacy service or new service | side-by-side | login, refresh, reconnect, and revoke flows pass parity checklist |
| Analytics/Telemetry | defer or replace | shared neutral format | side-by-side | event schema parity and dashboard continuity verified |
| Content Pipeline | wrap or replace | shared neutral format | slice-by-slice | import/export, validation, and authoring workflow pass |

## Ambiguity Register Rules

Create an `Ambiguity Register` entry whenever any of these is true:
- two or more dispositions look plausible
- parity is subjective and needs explicit sign-off
- ownership of data/content/runtime is unclear
- rollback is expensive or partially manual
- migration order depends on external tool or team decisions

Track each ambiguity with:
- subsystem
- current assumption
- options considered
- blocking evidence
- owner
- re-evaluation trigger

## Output Expectation

When subsystem-heavy migration is in scope, include a matrix or table that lists each affected subsystem with:
- disposition
- source of truth
- cutover mode
- parity gate
- rollback note
