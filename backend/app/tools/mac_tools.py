"""
Mac Tools

Reusable utilities for interacting with macOS.
"""

import subprocess


class MacTools:

    @staticmethod
    def open_app(app_name: str):
        """Open a macOS application."""
        print(f"Opening {app_name}...")
        subprocess.run(["open", "-a", app_name])

    @staticmethod
    def open_folder(folder_path: str):
        """Open a folder in Finder."""
        print(f"Opening folder: {folder_path}")
        subprocess.run(["open", folder_path])