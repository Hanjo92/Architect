# Output Template

Choose the output mode that matches the request scope.

## Compact Guidance

Use this for narrow asks that do not need a formal design package.

## 1) Context and Assumptions

- project type
- constraints
- missing inputs + explicit assumptions

## 2) Recommendation

- recommended structure, boundary decision, or architecture choice
- shortest rationale that explains why this is the right default

## 3) Key Rules

- dependency direction
- module/package boundaries
- naming or implementation rules only if they affect the recommendation

## 4) Next Steps

- 2-5 concrete follow-up actions

## Full Design Package

Use this exact section order for formal deliverables.

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

## 3.5) Domain Extraction Quality

- confidence score per domain
- evidence references per domain
- open questions for low-confidence domains

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

## 11) Ambiguity Register (Optional)

- ambiguous subsystem, runtime, or contract decision
- current assumption
- required evidence or parity proof
- owner and re-evaluation trigger

## 12) Migration Task Board Summary (Optional)

- task board link/path
- batch plan and current batch status
- done/in-progress/blocked counts
- next executable `Ready` tasks
- WIP/Blocked-SLA status and gate-owner assignment health

## 13) JSON Companion

- include machine-readable JSON following [output-json-format.md](output-json-format.md)
- keep section parity with Markdown output
