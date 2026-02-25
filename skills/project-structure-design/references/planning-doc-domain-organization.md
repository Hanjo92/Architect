# Planning Document Domain Organization

Use this guide when many planning documents exist in the project.

## Goal

Convert scattered planning docs into a domain-indexed map so architecture decisions are traceable.

## 1) Build Document Inventory

For each document collect:
- doc id/path
- topic summary
- last update date/owner (if available)
- confidence (`high`, `medium`, `low`)

## 2) Cluster by Domain

Map each document to one primary domain:
- Outgame domains (account, progression, economy, social, live-ops, monetization)
- Ingame domains (simulation, combat, movement, AI, stage runtime)
- Cross-cutting (contracts, observability, platform constraints)

Allow secondary tags only when needed.

## 3) Resolve Canonical Sources

- Detect overlap/conflict between docs in same domain.
- Mark one canonical source per domain.
- Mark others as `Supporting` or `Deprecated`.

## 4) Emit Domain Doc Map

Create a table like:

```markdown
| Doc | Primary Domain | Secondary Tags | Canonical | Status | Notes |
|---|---|---|---|---|---|
| docs/progression_v3.md | Progression | Economy | Yes | Active | baseline spec |
| docs/reward_notes.md | Economy | Progression | No | Supporting | reward edge cases |
```

## 5) Gap and Ambiguity Report

Include:
- missing domains with no doc coverage
- conflicting rules that block domain modeling
- clarification questions needed before final structure proposal

## Output Requirement

When this rule is used, include:
- document inventory count
- domain doc map table
- canonical source list
- unresolved conflict/gap list
