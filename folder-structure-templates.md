# Folder Structure Templates

## 1) Game Project Template

Assumption:
- Outgame: DDD
- Ingame: ECS
- Language/runtime examples are C# friendly

```text
game-project/
  src/
    outgame/
      contexts/
        account/
          domain/
          application/
          infrastructure/
        progression/
          domain/
          application/
          infrastructure/
        economy/
          domain/
          application/
          infrastructure/
        social/
          domain/
          application/
          infrastructure/
    ingame/
      ecs/
        entities/
        components/
        systems/
        pipelines/
      runtime/
      simulation/
    contracts/
      outgame-ingame/
  tools/
    content-pipeline/
    build/
  infra/
    ci/
    deploy/
  tests/
    outgame/
      unit/
      integration/
    ingame/
      simulation/
      performance/
  docs/
    architecture/
    adr/
```

Notes:
- Keep business/meta rules in `outgame/contexts/*`.
- Keep real-time loop logic in `ingame/ecs/*`.
- Exchange data only through `contracts/outgame-ingame/*`.

## 2) Web-App Service Template

Assumption:
- DDD + modular monolith first
- Feature-oriented package boundaries

```text
webapp-service/
  src/
    contexts/
      identity/
        domain/
        application/
        infrastructure/
        presentation/
      billing/
        domain/
        application/
        infrastructure/
        presentation/
      notification/
        domain/
        application/
        infrastructure/
        presentation/
    shared/
      kernel/
      contracts/
    bootstrap/
  api/
    http/
    grpc/
  jobs/
    workers/
    schedulers/
  infra/
    persistence/
    messaging/
    cache/
    observability/
  tests/
    unit/
    integration/
    e2e/
  docs/
    architecture/
    adr/
    runbooks/
  scripts/
    dev/
    release/
```

Notes:
- Keep dependency direction inward: `presentation/infrastructure -> application -> domain`.
- Keep `shared` minimal; avoid putting domain-specific rules there.
- Scale to microservices only when context boundaries and team ownership are stable.
- Apply clean-code naming conventions for modules/functions/types.
- Add concise function summary comments for non-trivial public functions (`XML docs` for C#, `TSDoc/JSDoc` for TS/JS).
