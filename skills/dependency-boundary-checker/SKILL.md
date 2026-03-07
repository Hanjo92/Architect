---
name: dependency-boundary-checker
description: Inspect repositories for dependency boundary violations, forbidden imports, layer leaks, and module coupling regressions. Use when users ask to review architecture conformance, check bounded-context or layer boundaries, verify DDD/Clean/Hexagonal rules, validate Unity or web-app module dependencies, or audit whether a migration preserved dependency direction.
---

# Dependency Boundary Checker

Use this skill to turn architecture rules into concrete dependency checks. Favor explicit findings over broad summaries, and verify real file-level references whenever possible.

Resolve bundled script paths relative to this `SKILL.md`. When this skill is installed into another repository, treat the containing folder as `<skill-root>` and run `<skill-root>/scripts/...`.

## Workflow

### 1) Identify the boundary model

Classify the repository before checking:
- DDD or modular monolith
- Clean/Hexagonal layered structure
- Unity game split (`Outgame(DDD)` / `Ingame(ECS)`)
- frontend/backend or service boundary
- migration compatibility boundary

Capture:
- which directories represent layers or modules
- which dependency directions are allowed
- which exceptions are intentional
- whether findings should be errors only or include warnings

If rules are already documented, encode them in a TOML config and run the checker.
If rules are not documented, infer the minimum safe rules from the repository structure and state the assumptions.

Read [boundary-rule-format.md](references/boundary-rule-format.md) for config shape.
Read [common-boundary-patterns.md](references/common-boundary-patterns.md) for starter rules.

### 2) Prefer explicit rules over guesswork

When a project has a stable architecture, write or update a config first.

Use these defaults unless the repository proves otherwise:
- domain must not depend on infrastructure or presentation
- application may depend on domain and contracts, but not concrete infrastructure implementations
- presentation must not bypass application use cases to reach infrastructure internals
- sibling bounded contexts must not reference each other's internals directly
- Unity `Ingame` must not depend on `Outgame` internals except through contracts/shared boundaries
- migration compatibility code must stay inside explicit compatibility or transition folders

### 3) Run the checker

Use the scanner from `<skill-root>`:

```bash
python3 <skill-root>/scripts/check_boundaries.py --root <repo-root> --config <repo-root>/dependency-boundaries.toml
```

Useful options:
- `--format text|json`
- `--include-warnings`
- `--fail-on warning|error`

If the repository has no config yet, create one from [common-boundary-patterns.md](references/common-boundary-patterns.md), then run the checker.

### 4) Review findings with architecture context

For each finding, explain:
- violated rule
- source file and import/reference
- why the dependency is risky
- the narrowest safe fix

Prioritize:
1. domain -> infrastructure/presentation leaks
2. cross-context internal references
3. migration compatibility boundary leaks
4. presentation or transport bypassing application contracts
5. warning-level coupling smells

### 5) Recommend enforceable follow-up

When the checker finds real issues, propose one or more of:
- move a type to contracts/shared kernel
- introduce an interface/port at the boundary
- invert dependency through application service or use case
- split compatibility code into a dedicated transition module
- add or tighten a config rule so the violation stays caught

When no findings are discovered, say that explicitly and note remaining blind spots such as reflection, dynamic loading, generated code, or dependencies not expressed as imports/usings.

## Output Contract

Return results in this order:
1. Boundary model and assumptions
2. Rule set used
3. Findings ordered by severity with file references
4. Blind spots or skipped areas
5. Recommended fixes or enforcement follow-up

Use compact Markdown by default.
Include JSON only when the user asks for machine-readable output or requests tool integration.

## Resources

### scripts/

- `check_boundaries.py`: scans repository files against TOML-defined boundary rules

### references/

- [boundary-rule-format.md](references/boundary-rule-format.md): config format and field meanings
- [common-boundary-patterns.md](references/common-boundary-patterns.md): starter rules for DDD, Unity, web-app, and migration boundaries
