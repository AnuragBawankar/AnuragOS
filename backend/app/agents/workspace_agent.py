"""
Workspace Agent

Responsible for preparing the AI development workspace.
"""

from app.config import WORKSPACE_APPS, AI_PROJECTS_FOLDER
from app.tools.mac_tools import MacTools


class WorkspaceAgent:

    def start(self):

        print("🚀 Starting AI Workspace...")

        for app in WORKSPACE_APPS:
            MacTools.open_app(app)

        MacTools.open_folder(AI_PROJECTS_FOLDER)

        print("\n✅ Workspace Ready")