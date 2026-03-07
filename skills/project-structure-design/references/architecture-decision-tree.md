# Architecture Decision Tree

Use this file at the beginning to select the right structure path.

## Step 1: Project Type

- If game project -> go to Step 2.
- If web-app/service project -> go to Step 5.

## Step 2: Game Split

- Always split:
  - Outgame -> DDD bounded contexts
  - Ingame -> ECS core loop

Then go to Step 3.

## Step 3: Multiplayer Requirement

- If multiplayer is required:
  - Define `Multiplayer/Abstractions/Ports` first.
  - Keep transport implementation in `Multiplayer/Transport`.
  - Keep Ingame unaware of concrete SDK implementations.
- If multiplayer is not required:
  - Use local loopback/null transport abstraction to keep future extensibility.

Then go to Step 4.

## Step 4: Runtime Mode

- `SinglePlayer`: local orchestration only
- `Host/Client`: shared contracts + transport adapter
- `DedicatedServer`: headless authoritative runtime

## Step 4.5: Unity UPM Modularization

- If Unity target and Outgame capability modules exist (ads/achievements/social):
  - Split each capability into independent UPM package.
  - Keep provider SDK integration inside package adapter layer.
  - Keep Ingame and app code dependent on package abstractions only.

## Step 4.7: Subsystem Migration Route

- If project is migrating between engines, major runtime stacks, or shared technical subsystems:
  - Inventory affected subsystems before proposing target structure.
  - Classify each subsystem with `retain`, `wrap`, `replace`, `defer`, or `drop`.
  - Assign one `Source of Truth` and one `Cutover Mode` per subsystem.
  - Define a concrete `Parity Gate` before moving traffic/content/runtime ownership.
  - Record unresolved cases in an `Ambiguity Register` instead of hiding them inside a generic roadmap.

## Step 5: Web-App / Service Path

- Start with DDD modular monolith.
- Use context-first folder structure.
- Use inward dependency direction.
- Promote to service split only when ownership and scaling pressures are explicit.

## Step 6: Coding Convention Path

- C#: clean naming + XML docs for non-trivial public functions.
- TS/JS: clean naming + TSDoc/JSDoc for non-trivial public functions.
