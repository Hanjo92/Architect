#!/usr/bin/env python3
"""Generate starter folder structures for game/web-app projects."""

from __future__ import annotations

import argparse
from pathlib import Path


def build_game_structure(unity: bool, multiplayer: bool, genre: str) -> list[str]:
    if unity:
        paths = [
            "Assets/_Game/Outgame/Contexts/Account/Domain",
            "Assets/_Game/Outgame/Contexts/Account/Application",
            "Assets/_Game/Outgame/Contexts/Account/Infrastructure",
            "Assets/_Game/Outgame/Contexts/Progression/Domain",
            "Assets/_Game/Outgame/Contexts/Progression/Application",
            "Assets/_Game/Outgame/Contexts/Progression/Infrastructure",
            "Assets/_Game/Outgame/Contexts/Economy/Domain",
            "Assets/_Game/Outgame/Contexts/Economy/Application",
            "Assets/_Game/Outgame/Contexts/Economy/Infrastructure",
            "Assets/_Game/Outgame/Contexts/Social/Domain",
            "Assets/_Game/Outgame/Contexts/Social/Application",
            "Assets/_Game/Outgame/Contexts/Social/Infrastructure",
            "Assets/_Game/Ingame/ECS/Entities",
            "Assets/_Game/Ingame/ECS/Components",
            "Assets/_Game/Ingame/ECS/Systems",
            "Assets/_Game/Ingame/ECS/Authoring",
            "Assets/_Game/Ingame/ECS/Bakers",
            "Assets/_Game/Ingame/ECS/Pipelines",
            "Assets/_Game/Ingame/Runtime",
            "Assets/_Game/Ingame/Simulation",
            "Assets/_Game/Integration/OutgameToIngame",
            "Assets/_Game/Integration/IngameToOutgame",
            "Assets/_Game/Shared/Kernel",
            "Assets/_Game/Shared/Contracts",
            "Assets/_Game/Bootstrap",
            "Assets/_Scenes",
            "Assets/_Addressables/Groups",
            "Assets/_Addressables/Profiles",
            "Packages",
            "ProjectSettings",
            "Tests/EditMode",
            "Tests/PlayMode",
            "Docs/Architecture",
            "Docs/ADR",
        ]

        # UPM capability modules for Unity Outgame domains.
        paths.extend(
            [
                "Packages/com.company.game.foundation/Runtime",
                "Packages/com.company.game.foundation/Editor",
                "Packages/com.company.game.ads/Runtime/Abstractions/Ports",
                "Packages/com.company.game.ads/Runtime/Abstractions/Contracts",
                "Packages/com.company.game.ads/Runtime/Application/UseCases",
                "Packages/com.company.game.ads/Runtime/Providers/UnityAdsAdapter",
                "Packages/com.company.game.ads/Editor",
                "Packages/com.company.game.ads/Tests/EditMode",
                "Packages/com.company.game.achievements/Runtime/Abstractions/Ports",
                "Packages/com.company.game.achievements/Runtime/Application/UseCases",
                "Packages/com.company.game.achievements/Runtime/Providers",
                "Packages/com.company.game.social/Runtime/Abstractions/Ports",
                "Packages/com.company.game.social/Runtime/Application/UseCases",
                "Packages/com.company.game.social/Runtime/Providers",
            ]
        )
    else:
        paths = [
            "src/outgame/contexts/account/domain",
            "src/outgame/contexts/account/application",
            "src/outgame/contexts/account/infrastructure",
            "src/outgame/contexts/progression/domain",
            "src/outgame/contexts/progression/application",
            "src/outgame/contexts/progression/infrastructure",
            "src/outgame/contexts/economy/domain",
            "src/outgame/contexts/economy/application",
            "src/outgame/contexts/economy/infrastructure",
            "src/ingame/ecs/entities",
            "src/ingame/ecs/components",
            "src/ingame/ecs/systems",
            "src/ingame/ecs/pipelines",
            "src/contracts/outgame-ingame",
            "tests/outgame/unit",
            "tests/ingame/simulation",
            "docs/architecture",
            "docs/adr",
        ]

    if multiplayer:
        if unity:
            paths.extend(
                [
                    "Assets/_Game/Multiplayer/Abstractions/Ports",
                    "Assets/_Game/Multiplayer/Abstractions/Contracts",
                    "Assets/_Game/Multiplayer/Application/Matchmaking",
                    "Assets/_Game/Multiplayer/Application/Session",
                    "Assets/_Game/Multiplayer/Application/Replication",
                    "Assets/_Game/Multiplayer/Transport/LocalLoopbackAdapter",
                    "Assets/_Game/Multiplayer/Transport/NetcodeAdapter",
                    "Assets/_Game/Multiplayer/DedicatedServer/Bootstrap",
                    "Assets/_Game/Integration/IngameToMultiplayer",
                    "Assets/_Game/Integration/MultiplayerToIngame",
                ]
            )
        else:
            paths.extend(
                [
                    "src/multiplayer/abstractions/ports",
                    "src/multiplayer/abstractions/contracts",
                    "src/multiplayer/application/session",
                    "src/multiplayer/transport",
                    "src/contracts/ingame-multiplayer",
                ]
            )
    return paths


def build_genre_paths(unity: bool, genre: str) -> list[str]:
    if genre == "casual":
        if unity:
            return [
                "Assets/_Game/Outgame/Contexts/LiveOps/Domain",
                "Assets/_Game/Outgame/Contexts/LiveOps/Application",
                "Assets/_Game/Outgame/Contexts/LiveOps/Infrastructure",
                "Assets/_Game/Outgame/Contexts/Analytics/Domain",
                "Assets/_Game/Outgame/Contexts/Analytics/Application",
                "Assets/_Game/Outgame/Contexts/Analytics/Infrastructure",
                "Assets/_Game/Ingame/Levels",
                "Assets/_Game/Ingame/StageRuntime",
            ]
        return [
            "src/outgame/contexts/liveops/domain",
            "src/outgame/contexts/liveops/application",
            "src/outgame/contexts/analytics/domain",
            "src/outgame/contexts/analytics/application",
            "src/ingame/levels",
            "src/ingame/stage-runtime",
        ]

    if genre == "rpg":
        if unity:
            return [
                "Assets/_Game/Outgame/Contexts/Inventory/Domain",
                "Assets/_Game/Outgame/Contexts/Inventory/Application",
                "Assets/_Game/Outgame/Contexts/Inventory/Infrastructure",
                "Assets/_Game/Outgame/Contexts/Equipment/Domain",
                "Assets/_Game/Outgame/Contexts/Equipment/Application",
                "Assets/_Game/Outgame/Contexts/Equipment/Infrastructure",
                "Assets/_Game/Outgame/Contexts/Quest/Domain",
                "Assets/_Game/Outgame/Contexts/Quest/Application",
                "Assets/_Game/Outgame/Contexts/Quest/Infrastructure",
                "Assets/_Game/Ingame/CombatRuntime",
                "Assets/_Game/Ingame/WorldSimulation",
                "Assets/_Game/Ingame/AIRuntime",
            ]
        return [
            "src/outgame/contexts/inventory/domain",
            "src/outgame/contexts/inventory/application",
            "src/outgame/contexts/equipment/domain",
            "src/outgame/contexts/equipment/application",
            "src/outgame/contexts/quest/domain",
            "src/outgame/contexts/quest/application",
            "src/ingame/combat-runtime",
            "src/ingame/world-simulation",
            "src/ingame/ai-runtime",
        ]

    return []


def build_webapp_structure() -> list[str]:
    return [
        "src/contexts/identity/domain",
        "src/contexts/identity/application",
        "src/contexts/identity/infrastructure",
        "src/contexts/identity/presentation",
        "src/contexts/billing/domain",
        "src/contexts/billing/application",
        "src/contexts/billing/infrastructure",
        "src/contexts/billing/presentation",
        "src/contexts/notification/domain",
        "src/contexts/notification/application",
        "src/contexts/notification/infrastructure",
        "src/contexts/notification/presentation",
        "src/shared/kernel",
        "src/shared/contracts",
        "src/bootstrap",
        "api/http",
        "api/grpc",
        "jobs/workers",
        "jobs/schedulers",
        "infra/persistence",
        "infra/messaging",
        "infra/cache",
        "infra/observability",
        "tests/unit",
        "tests/integration",
        "tests/e2e",
        "docs/architecture",
        "docs/adr",
        "docs/runbooks",
        "scripts/dev",
        "scripts/release",
    ]


def build_migration_structure(project_type: str, unity: bool) -> list[str]:
    if project_type == "game" and unity:
        return [
            "Assets/_Game/Compatibility/LegacyAdapters",
            "Assets/_Game/Compatibility/NewStackAdapters",
            "Assets/_Game/Transitions/Cutover",
            "Assets/_Game/Transitions/FeatureFlags",
            "Docs/Migration",
            "Docs/Migration/Evidence",
        ]

    if project_type == "game":
        return [
            "src/compatibility/legacy-adapters",
            "src/compatibility/new-stack-adapters",
            "src/transitions/cutover",
            "src/transitions/feature-flags",
            "docs/migration",
            "docs/migration/evidence",
        ]

    return [
        "src/shared/compatibility/legacy-adapters",
        "src/shared/compatibility/new-stack-adapters",
        "src/shared/transitions/cutover",
        "src/shared/transitions/feature-flags",
        "docs/migration",
        "docs/migration/evidence",
    ]


def build_migration_files(project_type: str, unity: bool) -> dict[str, str]:
    docs_root = "Docs/Migration" if project_type == "game" and unity else "docs/migration"
    return {
        f"{docs_root}/README.md": """# Migration Scaffold

Use this folder when the project needs staged migration across engines, runtimes, contracts, or other shared subsystems.

## Included Files

- `SubsystemClassification.md`: classify each affected subsystem with disposition, source of truth, cutover mode, and parity gate
- `AmbiguityRegister.md`: track unresolved migration decisions explicitly
- `TaskBoard.md`: seed execution tracking for reversible task batches

## Suggested Flow

1. Classify affected subsystems.
2. Define source of truth and cutover mode.
3. Record ambiguities before implementation starts.
4. Move only `Ready` tasks into execution.
""",
        f"{docs_root}/SubsystemClassification.md": """# Subsystem Classification

| Subsystem | Disposition | Source of Truth | Cutover Mode | Parity Gate | Rollback |
|---|---|---|---|---|---|
| Save/Load | wrap | shared neutral format | shadow/dual-run | old/new save files round-trip with equivalent state | route writes to legacy serializer |
| Session/Auth | replace | new stack | slice-by-slice | login, refresh, logout, and reconnect flows pass parity checklist | route affected clients to legacy auth gateway |
""",
        f"{docs_root}/AmbiguityRegister.md": """# Ambiguity Register

| Area | Current Assumption | Options Considered | Blocking Evidence | Owner | Re-evaluation Trigger |
|---|---|---|---|---|---|
| Asset Pipeline | Shared neutral export format is enough for transition | wrap legacy importer / replace importer / manual sync | import validation results pending | @owner | first content migration slice complete |
""",
        f"{docs_root}/TaskBoard.md": """# Migration Task Board

| Task ID | Domain/Slice | Scope | Disposition | Source of Truth | Cutover Mode | Parity Gate | Preconditions | Status | Owner | Risk | Rollback | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MIG-001 | Save/Load | Extract save format adapter | wrap | shared neutral format | shadow/dual-run | old/new save files round-trip with equivalent state | neutral schema agreed | Ready | @owner | Medium | route writes to legacy serializer | test-report-link |
| MIG-002 | Session/Auth | Move login/session flow to new backend contract | replace | new stack | slice-by-slice | login, refresh, logout, and reconnect flows pass contract parity checklist | MIG-001 done | Planned | @owner | High | route affected clients to legacy auth gateway | dashboard-link |
""",
    }


def create_directories(root: Path, paths: list[str], dry_run: bool) -> int:
    created = 0
    for rel in paths:
        path = root / rel
        if dry_run:
            print(f"[DRY-RUN] {path}")
            continue
        if not path.exists():
            created += 1
        path.mkdir(parents=True, exist_ok=True)
    return created


def create_files(root: Path, files: dict[str, str], dry_run: bool) -> int:
    created = 0
    for rel, content in files.items():
        path = root / rel
        if dry_run:
            print(f"[DRY-RUN] {path}")
            continue
        if not path.exists():
            created += 1
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    return created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate project folder structure.")
    parser.add_argument(
        "--project-type",
        choices=["game", "webapp"],
        required=True,
        help="Target project type.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output root directory where structure will be created.",
    )
    parser.add_argument(
        "--unity",
        action="store_true",
        help="Apply Unity-specific structure (game only).",
    )
    parser.add_argument(
        "--multiplayer",
        action="store_true",
        help="Include multiplayer module structure (game only).",
    )
    parser.add_argument(
        "--genre",
        choices=["common", "casual", "rpg"],
        default="common",
        help="Genre profile for game template extension (game only).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print structure without creating directories.",
    )
    parser.add_argument(
        "--with-migration-scaffold",
        action="store_true",
        help="Add compatibility, cutover, and migration documentation scaffold.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.output).resolve()

    if args.project_type == "webapp" and (args.unity or args.multiplayer or args.genre != "common"):
        print("Warning: --unity/--multiplayer/--genre flags are ignored for webapp.")

    if args.project_type == "game":
        paths = build_game_structure(unity=args.unity, multiplayer=args.multiplayer, genre=args.genre)
        paths.extend(build_genre_paths(unity=args.unity, genre=args.genre))
    else:
        paths = build_webapp_structure()

    files: dict[str, str] = {}
    if args.with_migration_scaffold:
        paths.extend(build_migration_structure(project_type=args.project_type, unity=args.unity))
        files = build_migration_files(project_type=args.project_type, unity=args.unity)

    created = create_directories(root, paths, args.dry_run)
    created_files = create_files(root, files, args.dry_run)
    if args.dry_run:
        print(
            f"Dry-run complete. Planned directories: {len(paths)}, planned files: {len(files)}"
        )
    else:
        print(
            "Done. "
            f"Total directories in template: {len(paths)}, newly created: {created}. "
            f"Template files created: {created_files}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
