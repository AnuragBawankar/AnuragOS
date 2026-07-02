"""
Mac Tools

Reusable utilities for interacting with macOS.
"""

import subprocess

from app.logger import logger


class MacTools:

    @staticmethod
    def open_app(app_name: str):
        """Open a macOS application."""
        logger.info(f"Opening application: {app_name}")
        subprocess.run(["open", "-a", app_name])

    @staticmethod
    def open_folder(folder_path: str):
        """Open a folder in Finder."""
        logger.info(f"Opening folder: {folder_path}")
        subprocess.run(["open", folder_path])