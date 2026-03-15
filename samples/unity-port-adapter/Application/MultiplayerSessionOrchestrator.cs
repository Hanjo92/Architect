using System;
using System.Collections.Generic;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using Game.Multiplayer.Abstractions;

namespace Game.Multiplayer.Application;

public sealed class MultiplayerSessionOrchestrator
{
    private readonly INetworkTransportPort _transport;
    private readonly List<PlayerId> _players = new();
    private SessionConfig? _sessionConfig;

    /// <summary>
    /// Create a session orchestrator that coordinates multiplayer flow through a transport port.
    /// </summary>
    /// <param name="transport">Transport port implementation selected by composition root.</param>
    public MultiplayerSessionOrchestrator(INetworkTransportPort transport)
    {
        _transport = transport;
        _transport.MessageReceived += OnTransportMessage;
        _transport.ConnectionChanged += _ => { };
    }

    /// <summary>
    /// Start multiplayer session orchestration for the selected runtime mode.
    /// </summary>
    /// <param name="mode">Runtime mode for transport and session execution.</param>
    /// <param name="config">Session configuration to initialize.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when orchestration startup is finished.</returns>
    public async Task StartAsync(RuntimeMode mode, SessionConfig config, CancellationToken ct = default)
    {
        _sessionConfig = config;
        await _transport.InitializeAsync(mode, config, ct);
    }

    /// <summary>
    /// Stop multiplayer session orchestration and shutdown transport.
    /// </summary>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when orchestration is stopped.</returns>
    public Task StopAsync(CancellationToken ct = default) => _transport.ShutdownAsync(ct);

    /// <summary>
    /// Publish local player input as a replication message to transport.
    /// </summary>
    /// <param name="playerId">Player identity that produced input.</param>
    /// <param name="inputJson">Serialized input payload.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when input message is sent.</returns>
    public Task PublishPlayerInputAsync(PlayerId playerId, string inputJson, CancellationToken ct = default)
    {
        var payload = new
        {
            playerId = playerId.Value,
            input = JsonSerializer.Deserialize<JsonElement>(inputJson)
        };

        var replicationMessage = new ReplicationMessage(
            MessageType: "PlayerInput",
            PayloadJson: JsonSerializer.Serialize(payload)
        );

        return _transport.SendAsync(replicationMessage, ct);
    }

    /// <summary>
    /// Return current session snapshot for diagnostics or UI projection.
    /// </summary>
    /// <returns>Current in-memory session snapshot.</returns>
    /// <exception cref="InvalidOperationException">Thrown when session has not been initialized.</exception>
    public SessionSnapshot GetSnapshot()
    {
        if (_sessionConfig is null)
        {
            throw new InvalidOperationException("Session is not initialized.");
        }

        return new SessionSnapshot(_sessionConfig.SessionId, _players.AsReadOnly());
    }

    /// <summary>
    /// Handle transport-level domain messages and project session state for current process.
    /// </summary>
    private void OnTransportMessage(ReplicationMessage message)
    {
        if (message.MessageType != "PlayerJoined")
        {
            return;
        }

        try
        {
            var payload = JsonSerializer.Deserialize<PlayerJoinedPayload>(message.PayloadJson);
            if (payload == null || string.IsNullOrEmpty(payload.playerId))
            {
                return;
            }

            var player = new PlayerId(payload.playerId);
            if (!_players.Contains(player))
            {
                _players.Add(player);
            }
        }
        catch (JsonException)
        {
            // Invalid JSON payload for PlayerJoined event
        }
    }

    private record PlayerJoinedPayload(string playerId);
}
