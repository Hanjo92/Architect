# Claude Platform Migration Notes

## 목표 / Goal

Codex 중심 스킬을 Claude 환경에서 사용 가능한 에이전트 자산으로 옮기기 위한 체크리스트입니다.  
This checklist helps migrate Codex-first skill assets into a Claude-compatible agent setup.

## 예상 차이 / Expected Differences

- `AGENTS.md` 직접 호환 여부 불명확  
  Direct `AGENTS.md` compatibility is uncertain.
- `SKILL.md`를 그대로 쓰기보다 Claude용 system/developer prompt 자산으로 재배치가 필요할 수 있음  
  `SKILL.md` may need to be restructured into Claude system/developer prompt assets.
- 로컬 스크립트 호출 방식과 권한 모델이 다를 수 있음  
  Local script invocation and permission rules may differ.

## 우선 전환 대상 / Priority Targets

- 구조 설계 원칙 / Architecture rules
- 출력 계약 / Output contract
- 도메인 추출 품질 기준 / Domain extraction quality rules
- 마이그레이션 태스크 보드 규칙 / Migration task board rules

## 체크리스트 / Checklist

- `SKILL.md` 내용을 Claude용 운영 프롬프트/플레이북으로 분리했는가  
  Split `SKILL.md` content into Claude-friendly prompt/playbook assets.
- `references/` 문서를 Claude 환경에서 읽기 쉬운 단위로 유지했는가  
  Keep `references/` in Claude-friendly chunks.
- 경로 예시를 Claude 환경에 맞게 상대경로 또는 일반 경로 설명으로 바꿨는가  
  Convert path examples into Claude-safe relative or generic paths.
- JSON 출력 규칙을 Claude 응답 형식에 맞게 유지했는가  
  Preserve JSON output rules in a Claude-compatible response shape.

## 템플릿 파일 / Template Files

- `CLAUDE.md.template`
- `system-prompt.template.md`
- `migration-config.json`
- `example-usage.md`

## 실제 사용 예시 / Example Usage

See `example-usage.md` for a ready-to-copy Claude invocation example.
See `sample-output.md` and `sample-output.json` for output-shape examples.

## 미해결 포인트 / Open Questions

- Claude 환경의 공식 스킬/에이전트 선언 포맷  
  Official Claude skill/agent declaration format
- Claude 환경에서의 로컬 검증 스크립트 실행 정책  
  Local validation script policy in Claude
