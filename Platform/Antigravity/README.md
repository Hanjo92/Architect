# Antigravity Platform Migration Notes

## 목표 / Goal

이 문서는 `project-structure-design` 자산을 Antigravity 환경으로 옮길 때 필요한 기준을 정리합니다.  
This document defines the baseline needed to migrate `project-structure-design` assets into an Antigravity environment.

## 예상 차이 / Expected Differences

- 스킬 등록 방식이 Codex와 다를 수 있음  
  Skill registration may differ from Codex.
- 참조 문서 로딩 방식이 다를 수 있음  
  Reference loading behavior may differ.
- 로컬 파일 실행/검증 권한 모델이 다를 수 있음  
  Local execution and validation permissions may differ.

## 전환 우선순위 / Migration Priorities

- 공통 개념 / Shared concepts:
  - DDD/ECS 분리 / DDD/ECS split
  - Unity UPM 모듈화 / Unity UPM modularization
  - 마이그레이션 태스크 보드 / Migration task board
  - 도메인 추출 품질 기준 / Domain extraction quality rules
- 플랫폼 고유 요소 / Platform-specific items:
  - 에이전트 선언 방식 / Agent declaration format
  - 프롬프트 라우팅 규칙 / Prompt routing rules
  - 검증 명령 실행 방식 / Validation command execution model

## 체크리스트 / Checklist

- 플랫폼 전용 에이전트 등록 문서를 만들었는가  
  Created platform-specific agent registration docs
- `references/` 중 핵심 문서를 우선 이식했는가  
  Migrated core `references/` first
- 샘플 출력(Markdown/JSON)이 플랫폼 UI에 맞는가  
  Confirmed Markdown/JSON sample outputs fit the platform UI
- 검증 단계가 실행 불가하면 대체 수동 체크리스트가 있는가  
  Added a fallback manual validation checklist when scripts are unavailable

## 권장 산출물 / Recommended Deliverables

- Antigravity용 platform-agent-guide / Antigravity platform agent guide
- 호환되는 출력 예시 1개 이상 / At least one compatible output example
- 제한사항/미지원 기능 목록 / Limits and unsupported features list

## 템플릿 파일 / Template Files

- `agent-config.template.yaml`
- `prompt-pack.template.md`
- `migration-config.json`
- `example-usage.md`

## 실제 사용 예시 / Example Usage

See `example-usage.md` for a concrete Antigravity-style example.
See `sample-output.md` and `sample-output.json` for output-shape examples.
