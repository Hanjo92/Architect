# Claude Example Usage

## 예시 목적 / Purpose

Codex용 `project-structure-design` 규칙을 Claude 환경에서 어떻게 호출하고 결과를 기대할지 보여주는 예시입니다.  
This example shows how to invoke the Codex-originated `project-structure-design` guidance in a Claude-style workflow.

## 입력 예시 / Input Example

```text
Use the project-structure-design guidance in this repository.
Analyze the planning docs below, extract domains, separate Outgame(DDD) and Ingame(ECS), and propose a Unity folder structure.

Planning docs:
- docs/core-loop.md
- docs/progression.md
- docs/economy.md

Return:
- concise Markdown report
- JSON companion
- confidence score and evidence refs per domain
```

## 기대 출력 / Expected Output

- planning augmentation summary if the docs are thin  
  Include planning augmentation summary when the docs are too thin.
- domain extraction summary with confidence/evidence  
  Include a domain extraction summary with confidence and evidence.
- Unity UPM package plan when applicable  
  Include a Unity UPM package plan when applicable.
- migration task board summary only when migration is in scope  
  Include migration task board summary only when migration is in scope.
