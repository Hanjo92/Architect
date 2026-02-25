# Unity UPM Modularization for Outgame Domains

Use this guide when the target is a Unity game and Outgame domains must be modularized.

## Package Split (Recommended)

- `com.company.game.foundation`
  - minimal shared abstractions (`Result`, domain event contracts, clock/id ports)
- `com.company.game.ads`
- `com.company.game.achievements`
- `com.company.game.social`

Keep domain policies inside each package. Keep foundation small and stable.

## Per-Package Internal Layout

```text
Packages/com.company.game.ads/
  package.json
  Runtime/
    Abstractions/
      Ports/
      Contracts/
    Application/
      UseCases/
    Providers/
      UnityAdsAdapter/
      AdMobAdapter/
  Editor/
  Tests/
    EditMode/
    PlayMode/
  Samples~
```

Apply the same pattern to achievements/social packages.

## Dependency Rules

- Game app and Outgame contexts reference only `Runtime/Abstractions`.
- `Providers/*Adapter` are selected in composition root.
- Ingame ECS must not call provider SDK directly.
- Cross-package domain logic coupling is disallowed (ads <-> social direct call forbidden).

## package.json Baseline

```json
{
  "name": "com.company.game.ads",
  "version": "1.0.0",
  "displayName": "Game Ads",
  "unity": "2022.3",
  "description": "Outgame ads domain module with provider adapters",
  "dependencies": {
    "com.company.game.foundation": "1.0.0"
  }
}
```

## asmdef Baseline

- `Game.Ads.Abstractions.asmdef`
- `Game.Ads.Application.asmdef` -> depends on `Game.Ads.Abstractions`
- `Game.Ads.Providers.asmdef` -> depends on `Game.Ads.Abstractions`

Do not allow `Application` -> `Providers` direct dependency.

## Versioning and Release

- Use semantic versioning.
- Require changelog and migration notes on minor/major updates.
- Keep backward-compatible contracts during migration windows.

## Output Requirement for Unity Requests

Include:
- package list and responsibilities
- package-level dependency graph
- port/adapter mapping per package
- rollout order (foundation -> ads/achievements/social)
