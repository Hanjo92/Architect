---
name: project-structure-design
description: Design project structure and system architecture for new or evolving software projects with a DDD-first approach and functional C# implementation guidance. For games, split Outgame(DDD) and Ingame(ECS), apply Unity UPM modularization, and keep multiplayer behind Port/Adapter boundaries. Support phased migration planning, including engine migration, runtime stack replacement, and ambiguous subsystem cutover decisions. Use for repository layout, bounded contexts, module boundaries, folder structure, architecture decisions, Unity/web-app structure, migration strategy, and requests like "프로젝트 구조 설계", "폴더 구조 추천", "유니티 폴더 구조", "UPM 패키지 구조", "엔진 마이그레이션", "엔진 업그레이드", and "마이그레이션 전략".
---

# Project Structure Design

Design structures with Domain-Driven Design as the default. Favor clear domain boundaries, explicit ubiquitous language, and implementation choices that protect aggregate invariants.
Resolve bundled script paths relative to this `SKILL.md`. When this skill is installed into another repository, treat the containing folder as `<skill-root>` and run `<skill-root>/scripts/...` commands instead of assuming the current working directory is the skill folder.

## Workflow

### 0) Route by decision tree

Choose path quickly:
- Is project a game?
- If yes: split into Outgame(DDD) and Ingame(ECS).
- If game has multiplayer: enforce Port/Adapter modular networking boundary.
- If not game (web-app/service): apply DDD + modular monolith first, then scale out.

Read [architecture-decision-tree.md](references/architecture-decision-tree.md) for full routing rules.

### 1) Capture design inputs

Extract or ask for:
- product scope and expected scale
- team size and ownership model
- deployment topology (single service, microservices, batch jobs, edge)
- non-functional priorities (speed, reliability, security, cost)
- constraints (must-use stack, cloud, deadline, legacy systems)

If key inputs are missing, proceed with explicit assumptions and continue.

### 1.2) Propose lightweight planning augmentation (when planning is thin)

If initial planning is too thin to derive reliable domains:
- propose a minimal augmentation checklist to reach baseline planning volume
- keep augmentation lightweight (one-page depth, not full design document)
- include only high-impact gaps: core loop, progression/economy intent, session/multiplayer mode, live-ops/monetization scope, platform constraints
- mark each added item as `Assumed`, `Proposed`, or `Confirmed`

Read [lightweight-planning-augmentation.md](references/lightweight-planning-augmentation.md).

### 1.5) Analyze game design document (when input is game planning)

When user provides game design/planning text:
- extract core loop, progression, economy, social, multiplayer, live-ops signals
- derive candidate domains and classify them into Outgame(DDD) vs Ingame(ECS)
- prioritize domains by delivery impact and technical risk
- score domain confidence and attach evidence references
- generate sample folder structures from chosen domains and boundaries

Read [game-design-analysis-playbook.md](references/game-design-analysis-playbook.md) and use [domain-catalog-template.md](references/domain-catalog-template.md).
Apply quality gates from [domain-extraction-quality-criteria.md](references/domain-extraction-quality-criteria.md).
Apply generation rules from [sample-folder-generator-rules.md](references/sample-folder-generator-rules.md).
For genre-agnostic baseline, refer to [samples/common-game/README.md](samples/common-game/README.md).
For genre-oriented baseline, refer to:
- [samples/casual-game/README.md](samples/casual-game/README.md)
- [samples/rpg-game/README.md](samples/rpg-game/README.md)

### 1.7) Organize planning docs by domain (when planning docs are many)

If project has many planning documents:
- inventory documents and cluster them by domain candidate
- identify duplicate/conflicting specs and mark canonical source per domain
- produce domain-indexed document map (doc -> domain -> confidence -> status)
- highlight missing/ambiguous domains requiring clarification

Read [planning-doc-domain-organization.md](references/planning-doc-domain-organization.md).

### 1.8) Classify subsystem migration ambiguity (when migrating shared runtime/tooling boundaries)

When project must move between engines, major engine versions, runtime stacks, or shared technical subsystems:
- inventory migration-coupled subsystems first: rendering, physics, input, animation, UI, scene/level flow, asset pipeline, save/load, networking, build tooling, editor tooling, backend contracts, analytics/telemetry, authentication/session, and content pipelines
- classify each subsystem with one `Disposition`: `retain`, `wrap`, `replace`, `defer`, or `drop`
- assign one `Source of Truth` during transition: `legacy engine`, `new engine`, `shared neutral format`, or `manual sync`
- assign one `Cutover Mode`: `side-by-side`, `shadow/dual-run`, `slice-by-slice`, or `big-bang`
- define one `Parity Gate` per subsystem before cutover: behavior parity, content parity, performance budget, determinism, or operational readiness
- record unresolved or high-risk cases in an `Ambiguity Register` with current assumption, blocking evidence, owner, and re-evaluation trigger

Read [subsystem-migration-decision-matrix.md](references/subsystem-migration-decision-matrix.md) before producing a migration plan that changes shared technical boundaries.

### 2) Select architecture style

Choose a DDD-first style:
- domain-oriented modular monolith (default)
- hexagonal/clean architecture with bounded contexts
- monorepo with domain packages per context
- service-oriented split by bounded context (only when team and ops maturity justify it)

State tradeoffs in one short table: why chosen, what risk remains.
Read [project-structure-blueprints.md](references/project-structure-blueprints.md) for baseline layouts when needed.

### 3) Design domain model boundaries

Define:
- bounded contexts and their responsibilities
- context map relations (upstream/downstream, anti-corruption layer needs)
- aggregates, entities, value objects, domain services
- invariants and transactional boundaries per aggregate

### 4) Define aggregate implementation pattern (Actor Model required)

When users request DDD aggregate implementation, use Actor Model as default:
- map each aggregate instance to one actor identity
- process commands sequentially per actor mailbox
- enforce invariants inside actor before state transitions
- emit domain events after successful transitions
- handle snapshots/recovery for stateful actors when needed

Read [ddd-actor-aggregate-pattern.md](references/ddd-actor-aggregate-pattern.md) when defining concrete implementation rules.

### 5) Define C# functional implementation rules

Apply functional style in C#:
- implement domain logic with feature-based `static class` + pure functions
- pass state as immutable record values and return new state
- model side effects as explicit ports/functions at application or infrastructure layer
- keep domain functions deterministic, composable, and test-first
- apply clean-code naming conventions for classes, functions, variables, and messages
- add concise function summary comments that state intent before implementation details

Read [csharp-functional-static-style.md](references/csharp-functional-static-style.md) when generating code and folder conventions.

### 6) Propose repository structure

Return a concrete tree with:
- top-level directories and purpose
- bounded context folders and ownership hints
- placement for tests, configs, docs, scripts, infra
- naming conventions (package/module boundaries, shared vs feature-local code)

Prefer context-first and feature-first grouping over purely technical grouping.
When user asks to materialize skeleton folders, run the generator from `<skill-root>`:
- `python3 <skill-root>/scripts/generate_structure.py --project-type game --unity --multiplayer --genre casual --output <target-dir>`
- `python3 <skill-root>/scripts/generate_structure.py --project-type game --unity --genre rpg --output <target-dir>`
- `python3 <skill-root>/scripts/generate_structure.py --project-type webapp --output <target-dir>`
- Add `--with-migration-scaffold` when user wants compatibility boundaries, ambiguity register, subsystem classification, or task board documents created with the initial structure.

### 7) Apply coding conventions (game and web-app)

Apply naming/comment rules across all project types:
- use clean-code naming conventions with intention-revealing names
- document non-trivial public functions with concise summary comments
- for C#, use XML docs (`summary`, `param`, `returns`, `exception`)
- for TypeScript/JavaScript web-apps, use TSDoc/JSDoc equivalents

Read [webapp-naming-comment-conventions.md](references/webapp-naming-comment-conventions.md) when producing web-app code standards.

### 8) Apply game-specific split rules (when project is a game)

Enforce two zones:
- Outgame (content/meta/live-ops/progression/store/social): design with DDD bounded contexts and aggregate rules.
- Ingame (real-time core gameplay loop): design with Entity-Component-System.

Rule:
- Do not force DDD aggregate boundaries inside the hot-path game loop.
- Do not force ECS for Outgame business domains.
- Define integration boundary between Outgame and Ingame via events/contracts.

Read [game-outgame-ddd-ingame-ecs.md](references/game-outgame-ddd-ingame-ecs.md) for structure and boundary rules.
If Unity is the target, apply [unity-upm-modularization.md](references/unity-upm-modularization.md).

### 9) Define decision records

List 5-10 architecture decisions:
- decision statement
- rationale
- alternatives considered
- impact and follow-up

Use [architecture-decision-checklist.md](references/architecture-decision-checklist.md) to avoid missing critical decisions.

### 10) Create phased implementation plan

Provide 3 phases:
- phase 1: ubiquitous language, bounded contexts, and aggregate contracts
- phase 2: actor-based aggregate implementation and integration
- phase 3: hardening, observability, recovery strategy, and scale-readiness

For each phase, include deliverables, risks, and done criteria.
When migrating existing systems, apply [migration-playbook.md](references/migration-playbook.md).
For medium/large migration, create and maintain [migration-task-board-template.md](references/migration-task-board-template.md), and execute migration by task status/checkpoints.
When migration involves engine/runtime replacement or any major subsystem swap, classify each affected subsystem with [subsystem-migration-decision-matrix.md](references/subsystem-migration-decision-matrix.md) and carry `Disposition`, `Source of Truth`, `Parity Gate`, and `Cutover Mode` into the task board.

### 11) Run validation gates

Always run the custom integrity validator before finalizing.
Run the base validator when the `quick_validate.py` script is available in the environment.
Resolve all validator paths from `<skill-root>`, not from the consumer repository root.

1. Base validator (when available):
   - `python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" <skill-root>`
   - If `$CODEX_HOME` is unset or `quick_validate.py` is unavailable, mark the base validator as `skipped` and state why.
2. Custom integrity validator:
   - `python3 <skill-root>/scripts/validate_skill_integrity.py`

Custom integrity validator checks:
- required reference files exist
- markdown links in `SKILL.md` resolve to existing local files
- critical rule phrases for game split, Unity UPM, naming/comment conventions are present

## Output Contract

Choose output mode by request scope:

1. `compact-guidance`
   - Use for narrow asks such as a folder tree recommendation, a bounded-context sketch, a quick Unity/web-app structure answer, or an architecture comparison.
   - Return concise Markdown only:
     - context and assumptions
     - recommended structure or boundary decision
     - key dependency rules or tradeoffs
     - next implementation steps
   - Include JSON only when the user explicitly asks for machine-readable output.

2. `full-design-package`
   - Use for formal architecture design, planning-doc analysis, migration planning, or whenever the user asks for a detailed deliverable.
   - Produce results in this order:
     1. Context and assumptions
     2. Planning augmentation summary (when initial planning is thin)
     3. Planning document domain map (when docs are many)
     4. Domain extraction summary from planning input (when provided)
     5. Domain extraction quality report (confidence + evidence + open questions)
     6. DDD model: bounded contexts, context map, aggregates
     7. Aggregate-to-actor mapping rules and concurrency model
     8. C# functional style rules (static class/function conventions)
     9. Game split rules (Outgame DDD / Ingame ECS) when applicable
     10. Unity UPM package modularization plan (when Unity game)
     11. Naming and function-comment conventions (game and web-app)
     12. Recommended architecture style and tradeoff table
     13. Proposed folder/repo tree
     14. Module responsibilities and dependency rules
     15. Key architecture decisions (ADR-style bullets)
     16. Phased implementation roadmap
     17. Optional migration path (only if legacy exists)
     18. Ambiguity Register (when migration contains unclear subsystem/runtime decisions)
     19. Validation gate result summary
     20. Migration task board summary (when migration is in scope)

Keep output concise and implementation-oriented. Avoid abstract theory unless directly tied to a decision.
For `full-design-package`, provide outputs in dual format:
- human-readable Markdown report
- machine-readable JSON companion following [output-json-format.md](references/output-json-format.md)

Always align final answer with [output-template.md](references/output-template.md).
Check forbidden design mistakes with [anti-patterns.md](references/anti-patterns.md) before finalizing.
Use [migration-playbook.md](references/migration-playbook.md) when migration is in scope.
Use [migration-task-board-template.md](references/migration-task-board-template.md) to track scope, progress, and rollback evidence.
