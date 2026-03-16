import pytest
from generate_structure import build_migration_structure

def test_build_migration_structure_game_unity():
    result = build_migration_structure("game", True)
    expected = [
        "Assets/_Game/Compatibility/LegacyAdapters",
        "Assets/_Game/Compatibility/NewStackAdapters",
        "Assets/_Game/Transitions/Cutover",
        "Assets/_Game/Transitions/FeatureFlags",
        "Docs/Migration",
        "Docs/Migration/Evidence",
    ]
    assert result == expected

def test_build_migration_structure_game_no_unity():
    result = build_migration_structure("game", False)
    expected = [
        "src/compatibility/legacy-adapters",
        "src/compatibility/new-stack-adapters",
        "src/transitions/cutover",
        "src/transitions/feature-flags",
        "docs/migration",
        "docs/migration/evidence",
    ]
    assert result == expected

def test_build_migration_structure_webapp():
    result = build_migration_structure("webapp", False)
    expected = [
        "src/shared/compatibility/legacy-adapters",
        "src/shared/compatibility/new-stack-adapters",
        "src/shared/transitions/cutover",
        "src/shared/transitions/feature-flags",
        "docs/migration",
        "docs/migration/evidence",
    ]
    assert result == expected
