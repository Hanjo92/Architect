# Platform

이 디렉터리는 `project-structure-design` 스킬과 관련 자산을 다른 에이전트/플랫폼 환경으로 이식할 때 필요한 문서와 체크리스트를 담습니다.  
This directory contains the documents and checklists needed to migrate `project-structure-design` assets to other agent/platform environments.

## 목적 / Purpose

- Codex 중심 구조를 다른 플랫폼으로 옮길 때 차이점을 명시적으로 관리  
  Manage differences explicitly when moving a Codex-first setup to another platform.
- 프롬프트, 파일 구조, 스킬/에이전트 메타데이터, 검증 절차를 플랫폼별로 정리  
  Organize prompts, file layout, skill/agent metadata, and validation steps per platform.
- 마이그레이션 중 공통으로 재사용할 수 있는 기준 문서 제공  
  Provide shared baseline documents that can be reused during migration.

## 구조 / Structure

- `Codex/`
  - 현재 기준 환경 / Current baseline environment
  - Codex 전용 스킬 경로, `AGENTS` 연동, 검증 방식 정리 / Codex-specific skill paths, `AGENTS` integration, and validation notes
- `Claude/`
  - Claude 환경 이식 시 필요한 프롬프트, 설정 템플릿, 사용 예시 / Prompting, config templates, and usage examples for Claude migration
- `Antigravity/`
  - Antigravity 환경 이식 시 필요한 설정 템플릿과 사용 예시 / Config templates and usage examples for Antigravity migration
- `platform-migration-manifest.template.json`
  - 플랫폼 전환 진행상황과 이슈를 추적하는 공통 매니페스트 / Shared manifest for tracking migration progress and issues
- `shared-migration-playbook.md`
  - 플랫폼 공통 마이그레이션 절차 / Shared migration procedure across platforms

## 사용 방법 / How To Use

1. 목표 플랫폼을 선택한다.  
   Choose the target platform.
2. 해당 플랫폼 디렉터리의 `README.md`를 기준으로 갭을 확인한다.  
   Review the target platform `README.md` to identify migration gaps.
3. 공통 작업은 `shared-migration-playbook.md`에 따라 태스크로 분리한다.  
   Split shared migration work into tasks using `shared-migration-playbook.md`.
4. 결과물은 플랫폼별 체크리스트와 예시에 따라 검증한다.  
   Validate deliverables against the platform-specific checklist and examples.
