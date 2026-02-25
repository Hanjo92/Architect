# Output JSON Format

Use this format when producing machine-readable companion output.

## Rules

- Keep keys stable and deterministic.
- Use `null` for non-applicable optional sections.
- Keep arrays ordered the same as Markdown section order.
- Add concise values; avoid verbose prose in JSON.

## Top-Level Shape

```json
{
  "meta": {
    "version": "1.0",
    "project_type": "game|webapp",
    "assumption_level": "low|medium|high"
  },
  "planning_augmentation": null,
  "planning_doc_domain_map": null,
  "domain_extraction": {
    "summary": "",
    "domains": []
  },
  "domain_extraction_quality": {
    "gates": {
      "critical_min": 0.75,
      "non_critical_min": 0.6
    },
    "per_domain": [],
    "open_questions": []
  },
  "ddd_model": {
    "bounded_contexts": [],
    "context_map": [],
    "aggregates": []
  },
  "actor_mapping": null,
  "coding_conventions": {
    "csharp": [],
    "ts_js": []
  },
  "game_split": null,
  "unity_upm_plan": null,
  "architecture_recommendation": {
    "style": "",
    "tradeoffs": []
  },
  "folder_tree": [],
  "dependency_rules": [],
  "adrs": [],
  "roadmap": [],
  "migration_plan": null,
  "migration_task_board": null,
  "validation_summary": {
    "base_validator": "pass|fail",
    "integrity_validator": "pass|fail"
  }
}
```

## Minimal Mapping Guidance

- `planning_augmentation`: include only when initial planning is thin.
- `planning_doc_domain_map`: include only when docs are many.
- `domain_extraction_quality`: include when domains are derived from planning docs.
- `game_split` and `unity_upm_plan`: include only for game projects.
- `migration_plan` and `migration_task_board`: include only when migration is in scope.
