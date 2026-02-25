# Domain Catalog Template

Use this template to summarize domains derived from game planning input.

```markdown
## Domain Catalog

| Domain | Zone | Purpose | Key Invariants | Interfaces | Priority |
|---|---|---|---|---|---|
| Account | Outgame(DDD) | Player profile and identity lifecycle | Unique identity, state consistency | Auth API, Social API | High |
| Progression | Outgame(DDD) | Level/skill/unlock progression | No invalid unlock transition | Reward, MatchResult | High |
| Economy | Outgame(DDD) | Currency/source/sink policy | No negative balance, atomic spend | Shop, Reward, Inventory | High |
| GameplaySimulation | Ingame(ECS) | Frame-based core gameplay simulation | Tick determinism constraints | Input stream, State snapshot | High |
| Combat | Ingame(ECS) | Damage/status/effect runtime | Rule ordering and bounds | Simulation systems | Medium |
```

## Required Notes

- Explain why each domain is Outgame(DDD) or Ingame(ECS).
- Mark cross-domain integration via contracts/events only.
- Call out top 3 high-risk boundaries.
