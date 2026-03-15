# Codex Sample Output

## Context and Assumptions

- Project type: Unity game
- Genre: common
- Planning depth: medium

## Domain Extraction Summary

- Outgame(DDD): Account, Progression, Monetization, Social
- Ingame(ECS): GameplaySimulation, StageRuntime, CharacterRuntime
- Multiplayer: optional, isolated behind Port/Adapter

## Architecture Recommendation

- Keep Outgame domain rules inside bounded contexts.
- Keep Ingame runtime loops inside ECS-oriented modules.
- Keep Ads, Achievements, and Social as independent UPM packages.
- Keep multiplayer SDK dependencies out of gameplay modules.

## Validation Notes

- Markdown output is intended for human review.
- JSON companion output is intended for automation and tooling.
- Validation should run with both base and integrity checks when available.

## Next Steps

1. Confirm the first bounded contexts and ECS runtime slices.
2. Generate the starter folder tree and UPM package skeletons.
3. Create the first implementation or migration batch.
