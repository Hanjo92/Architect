using System;
using System.Threading;
using System.Threading.Tasks;

namespace Game.Multiplayer.Abstractions;

public interface INetworkTransportPort
{
    /// <summary>
    /// Identify transport implementation name for diagnostics and runtime selection.
    /// </summary>
    string Name { get; }

    /// <summary>
    /// Receive replicated messages from remote or loopback transport.
    /// </summary>
    event Action<ReplicationMessage>? MessageReceived;

    /// <summary>
    /// Receive transport connection state changes.
    /// </summary>
    event Action<ConnectionState>? ConnectionChanged;

    /// <summary>
    /// Initialize transport for the given runtime mode and session configuration.
    /// </summary>
    /// <param name="mode">Runtime topology for transport behavior.</param>
    /// <param name="config">Session configuration used by the transport.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when initialization is finished.</returns>
    Task InitializeAsync(RuntimeMode mode, SessionConfig config, CancellationToken ct);

    /// <summary>
    /// Send a replication message through the selected transport.
    /// </summary>
    /// <param name="message">Replication payload to deliver.</param>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when send operation is accepted.</returns>
    Task SendAsync(ReplicationMessage message, CancellationToken ct);

    /// <summary>
    /// Shutdown transport and release network resources.
    /// </summary>
    /// <param name="ct">Cancellation token for cooperative cancellation.</param>
    /// <returns>A task that completes when shutdown is finished.</returns>
    Task ShutdownAsync(CancellationToken ct);
}
