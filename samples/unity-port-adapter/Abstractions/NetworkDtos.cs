using System;
using System.Collections.Generic;

namespace Game.Multiplayer.Abstractions;

/// <summary>
/// Represent runtime topology used to bootstrap multiplayer behavior.
/// </summary>
public enum RuntimeMode
{
    /// <summary>
    /// Run fully local simulation without remote peers.
    /// </summary>
    SinglePlayer,

    /// <summary>
    /// Run as host with local authority and remote clients.
    /// </summary>
    Host,

    /// <summary>
    /// Run as remote client connected to host or dedicated server.
    /// </summary>
    Client,

    /// <summary>
    /// Run as headless authoritative server.
    /// </summary>
    DedicatedServer
}

/// <summary>
/// Identify a player in a transport-agnostic way.
/// </summary>
/// <param name="Value">Stable player identifier.</param>
public readonly record struct PlayerId(string Value);

/// <summary>
/// Identify a multiplayer session in a transport-agnostic way.
/// </summary>
/// <param name="Value">Stable session identifier.</param>
public readonly record struct SessionId(string Value);

/// <summary>
/// Define immutable configuration required to initialize a session.
/// </summary>
/// <param name="SessionId">Target session identifier.</param>
/// <param name="MaxPlayers">Maximum number of players allowed in the session.</param>
/// <param name="MapId">Map identifier loaded for this session.</param>
public sealed record SessionConfig(
    SessionId SessionId,
    int MaxPlayers,
    string MapId
);

/// <summary>
/// Represent current session projection for diagnostics and UI.
/// </summary>
/// <param name="SessionId">Current session identifier.</param>
/// <param name="ConnectedPlayers">Connected players visible to orchestrator.</param>
public sealed record SessionSnapshot(
    SessionId SessionId,
    IReadOnlyList<PlayerId> ConnectedPlayers
);

/// <summary>
/// Carry replication payload across transport boundary.
/// </summary>
/// <param name="MessageType">Semantic message category.</param>
/// <param name="PayloadJson">Serialized message payload.</param>
public sealed record ReplicationMessage(
    string MessageType,
    string PayloadJson
);

/// <summary>
/// Represent transport connection lifecycle state.
/// </summary>
/// <param name="IsConnected">Whether transport is currently connected.</param>
/// <param name="TransportName">Active transport implementation name.</param>
/// <param name="CurrentSession">Current bound session when available.</param>
public sealed record ConnectionState(
    bool IsConnected,
    string TransportName,
    SessionId? CurrentSession
);
