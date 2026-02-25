# Project Structure Blueprints

Use this file when drafting concrete repository layouts.

## 1) DDD Modular Monolith (single app)

```text
repo/
  apps/
    api/
      src/
        contexts/
          billing/
            domain/
            application/
            infrastructure/
          identity/
            domain/
            application/
            infrastructure/
          notifications/
            domain/
            application/
            infrastructure/
        shared/
        main.ts
      tests/
  docs/
  scripts/
  infra/
```

Guidance:
- Keep `contexts/*` isolated; expose cross-context APIs explicitly.
- Keep `shared/` small; move domain logic back into each context.
- Place integration tests close to app boundary.
- When aggregate implementation uses Actor Model, place actor runtime adapters in each context's `infrastructure/actor/`.

## 2) Monorepo (multi app + shared packages)

```text
repo/
  apps/
    web/
    api/
    worker/
  packages/
    ui/
    domain/
    config/
    observability/
  infra/
  docs/
```

Guidance:
- Keep domain rules in `packages/domain`.
- Keep framework-specific code inside each `apps/*`.
- Enforce dependency direction: apps -> packages, not app-to-app.

## 3) Service-Oriented Split

```text
repo/
  services/
    user-service/
    order-service/
    payment-service/
  platform/
    gateway/
    shared-libs/
  ops/
    terraform/
    monitoring/
  docs/
```

Guidance:
- Split services only when independent deployment is required.
- Keep shared libraries minimal to avoid tight coupling.
- Define service contracts and ownership before splitting.

## 4) Game Split (Outgame DDD + Ingame ECS)

```text
repo/
  src/
    outgame/
      contexts/
        progression/
        economy/
        social/
    ingame/
      ecs/
        entities/
        components/
        systems/
        pipelines/
    contracts/
      outgame-ingame/
  tools/
  docs/
```

Guidance:
- Use DDD modeling only in `outgame/contexts/*`.
- Use ECS modeling only in `ingame/ecs/*`.
- Exchange data across boundary through contract DTO/event schemas.
- Keep game-loop performance logic isolated from outgame business rules.

## 5) Unity Outgame UPM Modules

```text
repo/
  Packages/
    com.company.game.foundation/
    com.company.game.ads/
    com.company.game.achievements/
    com.company.game.social/
  Assets/
    _Game/
      Ingame/
      CompositionRoot/
```

Guidance:
- Keep ads/achievements/social as independent UPM packages.
- Keep provider-specific SDK code inside each package's adapter/provider layer.
- Keep gameplay and app layers dependent on abstraction assemblies only.
- Roll out package adoption in order: foundation -> capability packages.

## Selection Heuristic

- Choose modular monolith by default.
- Choose monorepo when multiple apps share design systems or domain packages.
- Choose service split only with clear scaling/team boundaries and mature ops.
- For game projects, choose explicit Outgame/Ingame split with DDD/ECS separation.
- For Unity games with capability modules, prefer UPM package modularization.
