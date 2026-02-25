# Lightweight Planning Augmentation

Use this guide when initial project planning is too thin to derive stable domains.

## Goal

Reach minimum planning volume quickly without over-design.
Target: one-page augmentation that unblocks domain extraction and structure design.

## Minimum Augmentation Checklist

Fill at least one bullet per section:

1. Core Loop
- player/core user action loop
- win/fail or success criteria

2. Session and Runtime Mode
- single session shape (length, stage, match)
- single/multiplayer mode and authority assumption

3. Progression and Economy Intent (game) or Core Business Flow (web-app)
- progression direction and unlock policy (if game)
- economy source/sink policy (if game)
- core business transaction flow (if web-app/service)

4. Scope and Platform Constraints
- target platform/runtime
- must-have integrations and hard constraints

5. Live Features and Operations
- social/live-ops/monetization scope (if relevant)
- observability and release constraints

## Annotation Rule

Mark each augmentation item:
- `Assumed`: inferred from context
- `Proposed`: suggested by architect
- `Confirmed`: user/team validated

## Output Requirement

When augmentation is used, include:
- short “planning gap” summary
- augmentation checklist table with status labels
- impact note: how augmentation changed domain selection
