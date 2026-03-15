# Codex Platform Notes

## 현재 상태 / Current Status

이 저장소의 기준 플랫폼은 Codex입니다.  
Codex is the baseline platform for this repository.

## 주요 특성 / Key Characteristics

- `AGENTS.md` 기반 스킬 목록 사용  
  Uses `AGENTS.md` to register workspace skills
- `SKILL.md` 중심 스킬 구조  
  Uses `SKILL.md` as the primary skill artifact
- 로컬 파일 참조와 스크립트 실행이 직접 가능  
  Supports direct local file references and script execution
- `quick_validate.py`, `validate_skill_integrity.py` 같은 검증 스크립트 사용 가능  
  Supports validation scripts such as `quick_validate.py` and `validate_skill_integrity.py`

## 마이그레이션 관점 체크포인트 / Migration Checkpoints

- 기준 경로 / Baseline paths:
  - `skills/project-structure-design/SKILL.md`
  - `AGENTS.md`
- 전역 설치 경로 / Global install path:
  - `~/.codex/skills/project-structure-design/`
- 주요 검증 / Primary validation:
  - `python3 "$CODEX_HOME/skills/.system/skill-creator/scripts/quick_validate.py" skills/project-structure-design`
  - `python3 skills/project-structure-design/scripts/validate_skill_integrity.py`

## 템플릿 파일 / Template Files

- `AGENTS.template.md`
- `validation.config.json`
- `sample-output.md`
- `sample-output.json`

## 다른 플랫폼으로 넘길 때 확인할 것 / Check Before Moving To Another Platform

- `AGENTS.md` 개념이 그대로 있는가  
  Does the target platform support an `AGENTS`-style registry?
- `SKILL.md` frontmatter 규칙이 호환되는가  
  Is `SKILL.md` frontmatter compatible?
- 상대 경로 문서 링크를 그대로 해석하는가  
  Can it resolve relative document links as-is?
- Markdown과 JSON 동시 출력을 그대로 유지할 수 있는가  
  Can it preserve paired Markdown and JSON outputs?
