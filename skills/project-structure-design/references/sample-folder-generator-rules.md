# Sample Folder Generator Rules

Use these rules to generate sample folder structures from selected domains.

## Rule 1: Zone Split

- Always split `outgame/` and `ingame/` for game projects.
- Place DDD contexts only in `outgame/contexts/*`.
- Place ECS modules only in `ingame/ecs/*`.

## Rule 2: Domain-to-Folder Mapping

- Each Outgame domain gets:
  - `domain/`
  - `application/`
  - `infrastructure/`
  - `presentation/` (optional)
- Each Ingame domain gets:
  - `components/`
  - `systems/`
  - `authoring/` (Unity)
  - `pipelines/`

## Rule 3: Unity UPM Mapping (if Unity)

- Outgame capabilities (ads/achievements/social) become UPM packages under `Packages/`.
- Keep SDK-specific provider code under package adapter/provider layer.
- Keep project code dependent on abstraction assemblies only.

## Rule 4: Boundary Contracts

- Generate `contracts/outgame-ingame/` for DTO/event schemas.
- Do not share mutable runtime models across zones.

## Rule 5: Output Shape

Generated output must include:
- primary repository tree
- optional Unity `Packages/` tree
- short explanation per major folder

## Rule 6: Executable Generation

When user wants actual folder creation, run:

```bash
python3 <skill-root>/scripts/generate_structure.py --project-type game --unity --multiplayer --genre casual --output <target-dir>
python3 <skill-root>/scripts/generate_structure.py --project-type game --unity --genre rpg --output <target-dir>
python3 <skill-root>/scripts/generate_structure.py --project-type webapp --output <target-dir>
```

Use `--dry-run` first when user wants preview only.
Add `--with-migration-scaffold` when the project needs compatibility boundaries, migration docs, ambiguity tracking, or subsystem cutover planning from day one.
