using System;
using System.Threading;
using System.Threading.Tasks;
using Game.Multiplayer.Abstractions;

namespace Game.Multiplayer.Transport;

public sealed class NetcodeAdapterStub : INetworkTransportPort
{
    private SessionId? _sessionId;

    /// <summary>
    /// Return adapter name used by runtime diagnostics.
    /// </summary>
    public string Name => "NetcodeAdapterStub";

    /// <summary>
    /// Emit replicated messages received from transport implementation.
    /// </summary>
    public event Action<ReplicationMessage>? MessageReceived;

    /// <summary>
    /// Emit connection lifecycle changes from transport implementation.
    /// </summary>
    public event Action<ConnectionState>? ConnectionChanged;

    /// <summary>
    /// Initialize network adapter for the requested runtime mode.
    /// </summary>
    /// <param name="mode">Runtime mode requested by composition root.</param>
    /// <param name="config">Session configuration to bind adapter state.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when adapter initialization is finished.</returns>
    public Task InitializeAsync(RuntimeMode mode, SessionConfig config, CancellationToken ct)
    {
        _sessionId = config.SessionId;
        ConnectionChanged?.Invoke(new ConnectionState(
            IsConnected: true,
            TransportName: Name,
            CurrentSession: _sessionId
        ));
        return Task.CompletedTask;
    }

    /// <summary>
    /// Send a replication message through the network adapter.
    /// </summary>
    /// <param name="message">Replication payload to send.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when message send is accepted.</returns>
    public Task SendAsync(ReplicationMessage message, CancellationToken ct)
    {
        // Replace this with actual NGO/Photon send path.
        MessageReceived?.Invoke(message);
        return Task.CompletedTask;
    }

    /// <summary>
    /// Shutdown network adapter and emit disconnected state.
    /// </summary>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when adapter shutdown is finished.</returns>
    public Task ShutdownAsync(CancellationToken ct)
    {
        ConnectionChanged?.Invoke(new ConnectionState(
            IsConnected: false,
            TransportName: Name,
            CurrentSession: _sessionId
        ));
        return Task.CompletedTask;
    }
}
