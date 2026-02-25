# Anti-Patterns

Check this list before finalizing architecture guidance.

## Game Domain Anti-Patterns

- Putting Outgame DDD aggregate orchestration inside Ingame frame loop.
- Forcing ECS modeling on Outgame business domains like economy/progression.
- Allowing Ingame systems to call concrete transport SDK directly.
- Sharing mutable models between Outgame and Ingame without contracts.

## Multiplayer Anti-Patterns

- Binding gameplay logic directly to NGO/Photon APIs without port boundary.
- Mixing session policy and transport details in one class.
- Tight coupling between transport adapter and domain logic.
- Missing fallback mode (`LocalLoopback`/`Null`) for single-player operation.

## Unity UPM Anti-Patterns

- Putting ads/achievements/social in `Assets` monolithic managers instead of package modules.
- Exposing provider SDK types from package public abstraction contracts.
- Creating huge `foundation` package that contains domain-specific policies.
- Allowing direct dependency between capability packages (ads -> social).

## Web-App / Service Anti-Patterns

- Using generic utility buckets (`Utils`, `Manager`) as domain dumping ground.
- Coupling presentation/infrastructure directly to domain internals.
- Splitting into microservices before ownership/scaling boundaries are clear.
- Ignoring naming/comment conventions for public API behaviors.

## Documentation Anti-Patterns

- Writing comments that restate syntax, not intent.
- Missing param/returns/exception docs on non-trivial public methods.
- Inconsistent naming across folder, module, and domain terminology.
