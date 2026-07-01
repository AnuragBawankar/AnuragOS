"""
AnuragOS Orchestrator

Receives user commands and routes them to the appropriate agent.
"""

from app.core.registry import AgentRegistry


class Orchestrator:

    def __init__(self):
        print("🚀 AnuragOS Orchestrator initialized")
        self.registry = AgentRegistry()

    def execute(self, command: str):

        print(f"\nReceived command: {command}")

        agent = self.registry.get_agent(command)

        if agent:
            print(f"Selected Agent: {agent.__class__.__name__}")
            agent.start()
        else:
            print("❌ No suitable agent found.")