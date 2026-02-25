using System;
using System.Threading;
using System.Threading.Tasks;
using Game.Multiplayer.Abstractions;

namespace Game.Multiplayer.Transport;

public sealed class LocalLoopbackAdapter : INetworkTransportPort
{
    private SessionConfig? _config;

    /// <summary>
    /// Return adapter name used by runtime diagnostics.
    /// </summary>
    public string Name => "LocalLoopback";

    /// <summary>
    /// Emit messages as if they arrived from network for local simulation.
    /// </summary>
    public event Action<ReplicationMessage>? MessageReceived;

    /// <summary>
    /// Emit connection lifecycle changes for orchestration.
    /// </summary>
    public event Action<ConnectionState>? ConnectionChanged;

    /// <summary>
    /// Initialize local loopback transport and emit a synthetic local join event.
    /// </summary>
    /// <param name="mode">Runtime mode requested by composition root.</param>
    /// <param name="config">Session configuration used for local loopback.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when local transport is initialized.</returns>
    public Task InitializeAsync(RuntimeMode mode, SessionConfig config, CancellationToken ct)
    {
        _config = config;
        ConnectionChanged?.Invoke(new ConnectionState(
            IsConnected: true,
            TransportName: Name,
            CurrentSession: config.SessionId
        ));

        MessageReceived?.Invoke(new ReplicationMessage(
            "PlayerJoined",
            "{\"playerId\":\"local-player\"}"
        ));

        return Task.CompletedTask;
    }

    /// <summary>
    /// Send a message by immediately echoing it back through loopback.
    /// </summary>
    /// <param name="message">Replication payload to loop back.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A completed task after immediate loopback dispatch.</returns>
    public Task SendAsync(ReplicationMessage message, CancellationToken ct)
    {
        // Loopback simulates immediate echo from transport.
        MessageReceived?.Invoke(message);
        return Task.CompletedTask;
    }

    /// <summary>
    /// Shutdown loopback transport and emit disconnected state.
    /// </summary>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when shutdown event is emitted.</returns>
    public Task ShutdownAsync(CancellationToken ct)
    {
        ConnectionChanged?.Invoke(new ConnectionState(
            IsConnected: false,
            TransportName: Name,
            CurrentSession: _config?.SessionId
        ));
        return Task.CompletedTask;
    }
}
