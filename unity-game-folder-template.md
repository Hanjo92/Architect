# Unity Game Project Folder Template

## Goal

- Outgame: DDD 기반 컨텐츠/메타 시스템
- Ingame: ECS 기반 코어 게임플레이 루프
- Multiplayer: 코어 로직과 느슨하게 결합된 모듈형 네트워크 계층
- Unity 표준 디렉토리 구조 준수

## Template

```text
MyUnityGame/
  Assets/
    _Game/
      Outgame/
        Contexts/
          Account/
            Domain/
            Application/
            Infrastructure/
            Presentation/
          Progression/
            Domain/
            Application/
            Infrastructure/
            Presentation/
          Economy/
            Domain/
            Application/
            Infrastructure/
            Presentation/
          Social/
            Domain/
            Application/
            Infrastructure/
            Presentation/
        Contracts/
      Ingame/
        ECS/
          Entities/
          Components/
          Systems/
          Authoring/
          Bakers/
          Pipelines/
        Runtime/
        Simulation/
      Multiplayer/
        Abstractions/
          Ports/
          Contracts/
        Application/
          Matchmaking/
          Session/
          Replication/
        Transport/
          NetcodeAdapter/
          PhotonAdapter/
          CustomAdapter/
        DedicatedServer/
          Bootstrap/
          HeadlessRuntime/
        Testing/
          NetworkSimulation/
          LatencyProfiles/
      Integration/
        OutgameToIngame/
        IngameToOutgame/
        IngameToMultiplayer/
        MultiplayerToIngame/
      Shared/
        Kernel/
        Contracts/
        Utilities/
      Bootstrap/
      CompositionRoot/
    _Scenes/
      Bootstrap.unity
      Lobby.unity
      Gameplay.unity
    _Prefabs/
    _Addressables/
      Groups/
      Profiles/
    _UI/
    _Art/
      Materials/
      Textures/
      VFX/
      Animations/
    _Audio/
      BGM/
      SFX/
      Voice/
    _Data/
      ScriptableObjects/
      Localization/
  Packages/
    manifest.json
    packages-lock.json
  ProjectSettings/
  UserSettings/
  Logs/
  Temp/
  Library/
  Builds/
    Dev/
    Staging/
    Production/
  Tools/
    CI/
    ContentPipeline/
  Docs/
    Architecture/
    ADR/
    Runbooks/
  Tests/
    EditMode/
    PlayMode/
    Performance/
```

## Rules

- Outgame 규칙은 `Assets/_Game/Outgame/Contexts/*`에만 둔다.
- Ingame 프레임 루프 로직은 `Assets/_Game/Ingame/ECS/*`에만 둔다.
- Multiplayer 기능은 `Assets/_Game/Multiplayer/*`로 캡슐화한다.
- 경계 데이터 교환은 `Assets/_Game/Integration/*`와 `Contracts`를 통해서만 수행한다.
- 공통 코드(`Shared`)에는 도메인별 비즈니스 규칙을 넣지 않는다.

## Multiplayer Modularity Rules

- Ingame 시스템은 네트워크 SDK를 직접 호출하지 말고 `Multiplayer/Abstractions/Ports/*`만 참조한다.
- 네트워크 구현체(예: NGO, Photon)는 `Multiplayer/Transport/*Adapter`로 교체 가능해야 한다.
- 싱글플레이 모드에서는 `LocalLoopbackAdapter`(또는 Null Adapter)로 동작 가능해야 한다.
- 세션/매치메이킹/복제 정책은 Application 계층에서 정의하고, 전송 세부사항은 Transport 계층으로 격리한다.
- Outgame은 멀티플레이 세션 상태를 도메인 이벤트/계약으로만 관찰한다.

## Suggested asmdef Split (Loose Coupling)

```text
Assets/_Game/
  Ingame/
    Ingame.Core.asmdef
    Ingame.ECS.asmdef
  Multiplayer/
    Multiplayer.Abstractions.asmdef
    Multiplayer.Application.asmdef
    Multiplayer.Transport.asmdef
```

Dependency direction:
- `Ingame.*` -> `Multiplayer.Abstractions` (optional)
- `Multiplayer.Application` -> `Multiplayer.Abstractions`
- `Multiplayer.Transport` -> `Multiplayer.Abstractions`
- `Ingame.*` must not reference `Multiplayer.Transport`

## Runtime Mode Switching

Use composition root to select mode:
- `SinglePlayer`: Local adapter + local session orchestration
- `Host`: Local simulation + network publish
- `Client`: network-driven state sync + prediction/interpolation
- `DedicatedServer`: headless runtime + authoritative simulation

## Optional (DOTS-heavy)

If using DOTS extensively, split by assembly definition:

```text
Assets/_Game/Ingame/
  ECS.Core.asmdef
  ECS.Gameplay.asmdef
  ECS.Presentation.asmdef
```

And keep systems grouped by update phase:

```text
Assets/_Game/Ingame/ECS/Systems/
  Initialization/
  Simulation/
  Presentation/
```
