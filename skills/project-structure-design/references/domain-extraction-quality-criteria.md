# Domain Extraction Quality Criteria

Use this guide to enforce quality when deriving domains from planning input.

## Quality Dimensions

Score each extracted domain on:
- Boundary clarity (0.0-1.0)
- Responsibility clarity (0.0-1.0)
- Contract clarity (0.0-1.0)
- Evidence coverage (0.0-1.0)

Compute:
- `confidence_score = average(dimensions)`

## Evidence Requirement

For every domain, include:
- source docs used (path/id)
- key excerpt summary (short)
- reason for zone classification (Outgame DDD / Ingame ECS / Cross-cutting)

## Acceptance Gate

Minimum recommended gates:
- critical domains: confidence_score >= 0.75
- non-critical domains: confidence_score >= 0.60
- no domain without evidence links
- unresolved conflicts explicitly listed

## Escalation Rule

If confidence is below gate:
- request targeted clarification, or
- run lightweight planning augmentation, or
- keep domain as provisional with explicit risk tag

## Output Fields (per domain)

- `domain_name`
- `zone`
- `confidence_score`
- `evidence_refs[]`
- `open_questions[]`
- `risk_level`
