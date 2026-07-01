"""
Agent Registry

Maps commands to their corresponding agents.
"""

from app.agents.workspace_agent import WorkspaceAgent


class AgentRegistry:

    def __init__(self):
        self.agents = {
            "workspace": WorkspaceAgent()
        }

    def get_agent(self, command: str):

        command = command.lower()

        for keyword, agent in self.agents.items():

            if keyword in command:
                return agent

        return None