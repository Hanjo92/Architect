# Architecture Decision Checklist

Use this checklist before finalizing the structure proposal.

## Scope and Boundaries

- Are domain boundaries explicit and named consistently?
- Is ownership clear per module/service/package?
- Are cross-boundary dependencies minimized?

## Dependency Rules

- Is dependency direction documented (what can import what)?
- Are shared utilities prevented from becoming a dumping ground?
- Are external integrations isolated behind adapters/ports?

## Data and State

- Is the source of truth clear per domain?
- Are transaction boundaries defined?
- Are caching and consistency tradeoffs explicit?

## Runtime and Delivery

- Are deployment units and environments defined?
- Are configuration/secrets management locations defined?
- Are background jobs and async workflows placed intentionally?

## Quality and Operations

- Are test layers defined (unit/integration/e2e)?
- Are observability hooks defined (logs/metrics/traces)?
- Are failure modes and fallback behavior identified?

## Team and Evolution

- Does structure support current team topology?
- Is there a migration path from current state to target state?
- Are top 3 technical risks and mitigations listed?

## Game Split (only for game projects)

- Is Outgame explicitly modeled as DDD bounded contexts?
- Is Ingame explicitly modeled as ECS runtime?
- Are Outgame and Ingame integration contracts versioned?
- Are game-loop systems protected from outgame domain coupling?
