# Domain Catalog Template

Use this template to summarize domains derived from game planning input.

```markdown
## Domain Catalog

| Domain | Zone | Purpose | Key Invariants | Interfaces | Priority | Confidence | Evidence |
|---|---|---|---|---|---|---|---|
| Account | Outgame(DDD) | Player profile and identity lifecycle | Unique identity, state consistency | Auth API, Social API | High | 0.82 | docs/account.md |
| Progression | Outgame(DDD) | Level/skill/unlock progression | No invalid unlock transition | Reward, MatchResult | High | 0.80 | docs/progression.md |
| Economy | Outgame(DDD) | Currency/source/sink policy | No negative balance, atomic spend | Shop, Reward, Inventory | High | 0.78 | docs/economy.md |
| GameplaySimulation | Ingame(ECS) | Frame-based core gameplay simulation | Tick determinism constraints | Input stream, State snapshot | High | 0.84 | docs/gameplay-loop.md |
| Combat | Ingame(ECS) | Damage/status/effect runtime | Rule ordering and bounds | Simulation systems | Medium | 0.69 | docs/combat-notes.md |
```

## Required Notes

- Explain why each domain is Outgame(DDD) or Ingame(ECS).
- Mark cross-domain integration via contracts/events only.
- Call out top 3 high-risk boundaries.
- Include confidence score and evidence references per domain.
- List open questions for domains below quality gate.
