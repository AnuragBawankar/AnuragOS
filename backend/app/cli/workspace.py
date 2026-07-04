"""
Workspace CLI command.
"""

from app.core.orchestrator import Orchestrator


def workspace_command(args):
    """
    Start the AI Workspace.
    """
    orchestrator = Orchestrator()
    orchestrator.execute("Start AI Workspace")