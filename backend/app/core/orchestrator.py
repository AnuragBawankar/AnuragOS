"""
AnuragOS Orchestrator

Receives user commands and routes them to the appropriate agent.
"""

from app.core.registry import AgentRegistry
from app.logger import logger


class Orchestrator:

    def __init__(self):
        logger.info("AnuragOS Orchestrator initialized")
        self.registry = AgentRegistry()

    def execute(self, command: str):

        logger.info(f"Received command: {command}")

        agent = self.registry.get_agent(command)

        if agent:
            logger.info(f"Selected Agent: {agent.__class__.__name__}")
            agent.start()
        else:
            logger.warning("No suitable agent found.")