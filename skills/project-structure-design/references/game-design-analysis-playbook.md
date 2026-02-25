# Game Design Analysis Playbook

Use this playbook when the user provides a game planning/design document.

## 0) Check Planning Sufficiency

If planning detail is too low to infer domains:
- run [lightweight-planning-augmentation.md](lightweight-planning-augmentation.md)
- annotate added items as `Assumed`, `Proposed`, `Confirmed`
- then continue with domain extraction

If planning documents are many, run [planning-doc-domain-organization.md](planning-doc-domain-organization.md) first.

## 1) Parse Planning Signals

Extract:
- core gameplay loop (combat, puzzle, build, race, etc.)
- session structure (single run, match, stage, endless)
- progression model (level, skill tree, equipment, account progression)
- economy model (currencies, sinks/sources, shop, rewards)
- social/live features (friends, guild, ranking, events, pass)
- multiplayer and authority model (P2P, host-client, dedicated)

## 2) Derive Candidate Domains

Create candidate domain list:
- Outgame candidates: account, progression, economy, social, live-ops, monetization
- Ingame candidates: gameplay simulation, combat, movement, AI, physics, stage runtime

## 3) Classify by Architecture

- Outgame -> DDD bounded context
- Ingame -> ECS module
- shared contracts -> event/message schemas only

Reject mixed models in same hot path.

## 4) Prioritize Domains

Score each domain:
- delivery impact (high/medium/low)
- uncertainty risk (high/medium/low)
- coupling risk (high/medium/low)

Use score to sequence implementation phases.

## 5) Emit Design Output

Must include:
- extracted planning summary
- domain catalog table
- outgame/ingame split map
- sample folder tree
- UPM package split (Unity)
- 3-phase rollout and ADR highlights
