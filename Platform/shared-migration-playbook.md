# Shared Platform Migration Playbook

이 문서는 Codex, Claude, Antigravity 환경 사이에서 스킬/문서/운영 방식을 옮길 때 공통으로 따르는 절차를 정의합니다.  
This document defines the shared process for moving skills, docs, and operating conventions across Codex, Claude, and Antigravity.

## 1) 현재 자산 인벤토리 / Current Asset Inventory

- 스킬 본체: `skills/project-structure-design/` / Primary skill assets
- 보조 스킬: `skills/dependency-boundary-checker/` / Supporting skill assets
- 문서: `README.md`, `AGENTS.md` / Root documentation and workspace registration
- 샘플: `samples/`, `skills/project-structure-design/samples/` / Shared and skill-local examples

## 2) 플랫폼 차이 식별 / Identify Platform Differences

- 스킬/에이전트 선언 파일 형식 / Skill or agent declaration format
- 프롬프트 호출 방식 / Prompt invocation style
- 절대/상대 경로 허용 범위 / Absolute or relative path behavior
- 검증 스크립트 실행 환경 / Validation script execution model
- 샘플/참조 문서 로딩 방식 / Sample and reference loading behavior

## 3) 이식 단위 분리 / Split Migration Units

- `Prompting`
- `Skill Metadata`
- `References`
- `Samples`
- `Validation`
- `Docs`

각 단위는 독립 태스크로 쪼개고 플랫폼별 체크리스트에 연결합니다.  
Split each unit into independent tasks and attach them to the target platform checklist.

## 4) 공통 산출물 / Shared Deliverables

- 플랫폼별 README / Platform-specific README
- 차이 요약표 / Difference summary
- 실행/검증 체크리스트 / Execution and validation checklist
- 미해결 이슈 목록 / Open issues list

## 5) 검증 게이트 / Validation Gates

- 주요 문서 경로가 해당 플랫폼에서 해석 가능한가 / Can the platform resolve key document paths?
- 스킬 호출 예시가 실제 사용 가능한가 / Are invocation examples actually usable?
- 검증 절차가 해당 플랫폼에서 실행 가능한가 / Can validation steps run in that platform?
- 플랫폼별 제한사항이 명시되었는가 / Are platform-specific limitations documented?

## 6) 운영 원칙 / Operating Principles

- 플랫폼별 문서는 공통 개념을 복제하지 말고 차이만 강조 / Platform docs should emphasize differences rather than duplicate shared concepts
- 공통 원칙은 이 문서에 유지 / Keep shared principles in this file
- 플랫폼 고유 명령/제약은 각 하위 README에서만 관리 / Keep platform-specific commands and constraints only in platform sub-readmes
