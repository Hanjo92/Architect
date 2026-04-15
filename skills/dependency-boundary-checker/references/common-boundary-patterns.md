# Common Boundary Patterns

Use these patterns to bootstrap a repository config quickly.

## 1) DDD / Modular Monolith

Start with:
- domain must not reference infrastructure or presentation
- application must not reference infrastructure internals directly
- sibling contexts must not depend on each other's internals

Suggested config fragments:

These rules match dependency strings such as C# namespaces, not source file paths.
For C# examples, use your solution's root namespace in the regex rather than a filesystem pattern.

```toml
[[rules]]
name = "domain-no-infra-or-presentation"
severity = "error"
source_globs = ["src/contexts/*/domain/**/*.cs"]
forbidden_patterns = ['\\.Infrastructure\\.', '\\.Presentation\\.']
message = "Domain code must stay free of infrastructure and presentation dependencies."

[[rules]]
name = "cross-context-internals"
severity = "warning"
source_globs = ["src/contexts/**/*.cs"]
forbidden_patterns = ['^Acme\\.Product\\.Contexts\\.[A-Za-z0-9_]+\\.(Domain|Application|Infrastructure)\\.']
allowed_patterns = ['\\.Contracts\\.', '\\.Shared\\.']
message = "Check whether bounded contexts are reaching into each other's internal layers through direct namespace references."
```

When writing regex patterns in TOML, prefer single-quoted strings:

```toml
forbidden_patterns = ['\\.Infrastructure\\.', '\\.Presentation\\.']
```

## 2) Unity Game Split

Start with:
- `Ingame` must not import `Outgame` internals
- capability packages must not reference each other directly
- transport SDKs must stay behind multiplayer adapters

Suggested checks:
- `Assets/_Game/Ingame/**/*.cs` cannot reference `Outgame.Contexts.*.(Domain|Application|Infrastructure)`
- `Packages/com.company.game.ads/**` cannot reference `Packages/com.company.game.social/**`
- `Assets/_Game/Ingame/**/*.cs` cannot reference NGO/Photon concrete APIs directly

## 3) Web-App Layered Structure

Start with:
- presentation/UI should call application/use-case layer, not infrastructure internals
- infrastructure should not depend on presentation
- shared contracts are allowed, shared utility dumping grounds are not

Suggested checks:
- `src/**/presentation/**/*` cannot reference `/infrastructure/`
- `src/**/infrastructure/**/*` cannot reference `/presentation/`

## 4) Migration Compatibility Boundary

Start with:
- compatibility adapters should stay in dedicated compatibility/transition folders
- legacy and new stack code should not both own the same source of truth without explicit rule
- temporary bridges should be warning-level findings outside migration folders

Suggested checks:
- `LegacyAdapter`, `CompatibilityBridge`, `TransitionFacade` names outside `compatibility/` or `transitions/`
- direct imports from `legacy/` into stable domain/application code

## 5) Output Expectations

A good review should identify:
- rule violated
- exact source file
- imported namespace/module
- minimal fix
- whether the rule should be tightened or relaxed
