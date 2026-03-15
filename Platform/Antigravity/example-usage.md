# Antigravity Example Usage

## 예시 목적 / Purpose

Antigravity 환경에서 `project-structure-design` 자산을 활용해 구조 설계를 요청하는 형태를 보여줍니다.  
This example shows how to request architecture guidance in an Antigravity-style environment using `project-structure-design` assets.

## 입력 예시 / Input Example

```text
Apply the project-structure-design rules from the repository assets.
We are planning a Unity casual game with lightweight multiplayer.

Inputs:
- docs/overview.md
- docs/stage-design.md
- docs/liveops.md

Tasks:
- organize docs by domain
- derive Outgame(DDD) and Ingame(ECS) boundaries
- generate a starter folder tree
- include Markdown + JSON output
```

## 기대 출력 / Expected Output

- domain-indexed planning doc map  
  Return a domain-indexed planning doc map.
- casual-genre-oriented Outgame/Ingame split  
  Return a casual-genre-oriented Outgame/Ingame split.
- Port/Adapter multiplayer boundary  
  Return a Port/Adapter multiplayer boundary.
- starter folder tree and next steps  
  Return a starter folder tree and next steps.
