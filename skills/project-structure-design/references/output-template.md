# Output Template

Use this exact section order for consistent deliverables.

## 1) Context and Assumptions

- project type
- constraints
- missing inputs + explicit assumptions

## 2) Decision Tree Result

- selected path (game/web-app)
- selected split (Outgame/Ingame if game)
- multiplayer boundary decision (if game)

## 3) Domain Model and Boundaries

- bounded contexts and responsibilities
- context map and integration boundaries
- aggregates and invariants (Outgame only for games)

## 4) Implementation Style Rules

- C# functional static-style rules
- naming conventions
- function-comment conventions (XML/TSDoc/JSDoc)

## 5) Architecture Recommendation and Tradeoffs

- recommended style
- alternatives considered
- tradeoff table

## 6) Proposed Folder Tree

- concrete repo tree
- purpose per top-level folder

## 7) Dependency and Integration Rules

- dependency direction
- contract boundaries
- multiplayer port/adapter rules (if game)

## 8) Key Architecture Decisions (ADR-style)

- 5-10 concise decision bullets with rationale

## 9) Phased Roadmap

- phase 1/2/3 deliverables
- risk and done criteria per phase

## 10) Migration Plan (Optional)

- current -> target transition steps
- rollback and risk controls
- strangler slice order and compatibility boundary
- contract versioning and observability gates

## 11) Migration Task Board Summary (Optional)

- task board link/path
- batch plan and current batch status
- done/in-progress/blocked counts
- next executable `Ready` tasks
