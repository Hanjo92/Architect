using Game.Multiplayer.Abstractions;
using Game.Multiplayer.Application;
using Game.Multiplayer.Transport;

namespace Game.Multiplayer.CompositionRoot;

public static class MultiplayerCompositionRoot
{
    /// <summary>
    /// Create multiplayer orchestrator with transport adapter selected by runtime mode.
    /// </summary>
    /// <param name="mode">Runtime mode that determines selected transport adapter.</param>
    /// <returns>Configured multiplayer session orchestrator.</returns>
    public static MultiplayerSessionOrchestrator Create(RuntimeMode mode)
    {
        INetworkTransportPort transport = mode switch
        {
            RuntimeMode.SinglePlayer => new LocalLoopbackAdapter(),
            RuntimeMode.Host => new NetcodeAdapterStub(),
            RuntimeMode.Client => new NetcodeAdapterStub(),
            RuntimeMode.DedicatedServer => new NetcodeAdapterStub(),
            _ => new LocalLoopbackAdapter()
        };

        return new MultiplayerSessionOrchestrator(transport);
    }
}
