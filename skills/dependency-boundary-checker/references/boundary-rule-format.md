# Boundary Rule Format

Use a TOML file to define enforceable dependency rules.

## File Name

Recommended names:
- `dependency-boundaries.toml`
- `.dependency-boundaries.toml`

## Top-Level Fields

```toml
include_warnings = true
exclude = ["**/bin/**", "**/obj/**", "**/node_modules/**", "**/Library/**"]

[[rules]]
name = "domain-no-infra"
severity = "error"
source_globs = ["src/contexts/*/domain/**/*.cs"]
forbidden_patterns = [
  '\\.Infrastructure\\.',
  '\\.Presentation\\.'
]
allowed_patterns = [
  '\\.Domain\\.',
  '\\.Contracts\\.'
]
message = "Domain code must not depend on infrastructure or presentation types."
```

## Rule Fields

- `name`: stable identifier for the rule
- `severity`: `error` or `warning`
- `source_globs`: files to check
- `forbidden_patterns`: regex patterns matched against extracted dependency strings
- `allowed_patterns`: optional regex patterns that suppress a match
- `message`: human-readable explanation shown in findings

## Supported Dependency Extraction

The checker reads direct dependency statements from:
- C#: `using Namespace.Type;`
- JS/TS: `import ... from 'module'`, `export ... from 'module'`, `require('module')`
- Python: `import x`, `from x import y`

The checker is intentionally static and conservative:
- it does not execute code
- it does not resolve runtime reflection
- it does not expand generated code semantics beyond plain text scanning

## Path Filtering Guidance

Use narrow `source_globs` whenever possible.

Good:
- `src/contexts/*/domain/**/*.cs`
- `Assets/_Game/Outgame/Contexts/*/Domain/**/*.cs`

Too broad:
- `src/**/*.cs`

## Example Rule Sets

### DDD Layer Rule

```toml
[[rules]]
name = "application-no-infra-direct"
severity = "error"
source_globs = ["src/contexts/*/application/**/*.cs"]
forbidden_patterns = [
  '\\.Infrastructure\\.'
]
message = "Application layer must depend on ports/contracts, not concrete infrastructure."
```

### Unity Game Split Rule

```toml
[[rules]]
name = "ingame-no-outgame-internals"
severity = "error"
source_globs = ["Assets/_Game/Ingame/**/*.cs"]
forbidden_patterns = [
  'Outgame\\.Contexts\\..+\\.(Domain|Application|Infrastructure)'
]
allowed_patterns = [
  'Shared\\.',
  'Contracts\\.'
]
message = "Ingame code must not depend on Outgame internals."
```

### Migration Compatibility Warning

```toml
[[rules]]
name = "compatibility-code-contained"
severity = "warning"
source_globs = ["src/**/*.cs", "src/**/*.ts"]
forbidden_patterns = [
  'LegacyAdapter',
  'CompatibilityBridge',
  'TransitionFacade'
]
allowed_patterns = [
  'src/compatibility/',
  'src/transitions/'
]
message = "Compatibility code should remain inside explicit migration boundaries."
```

Use single-quoted TOML strings for regex patterns. Plain double-quoted TOML strings treat backslashes as escapes and will fail for patterns like `\.` unless every backslash is doubled again.
