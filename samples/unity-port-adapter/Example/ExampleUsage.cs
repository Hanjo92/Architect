using System;
using System.Threading.Tasks;
using Game.Multiplayer.Abstractions;
using Game.Multiplayer.CompositionRoot;

namespace Game.Multiplayer.Example;

public static class ExampleUsage
{
    /// <summary>
    /// Demonstrate end-to-end multiplayer orchestration using single-player loopback transport.
    /// </summary>
    /// <returns>A task that completes after sample session run and shutdown.</returns>
    public static async Task RunAsync()
    {
        var mode = RuntimeMode.SinglePlayer;
        var orchestrator = MultiplayerCompositionRoot.Create(mode);

        var config = new SessionConfig(
            SessionId: new SessionId("session-local-001"),
            MaxPlayers: 4,
            MapId: "arena-01"
        );

        await orchestrator.StartAsync(mode, config);
        await orchestrator.PublishPlayerInputAsync(new PlayerId("local-player"), "{\"move\":\"left\"}");

        var snapshot = orchestrator.GetSnapshot();
        Console.WriteLine($"Session={snapshot.SessionId.Value}, Players={snapshot.ConnectedPlayers.Count}");

        await orchestrator.StopAsync();
    }
}
