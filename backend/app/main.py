import sys

from app.core.orchestrator import Orchestrator


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print('uv run python -m app.main "Your Command"')
        return

    command = " ".join(sys.argv[1:])

    if command.lower() == "help":
        print("\nAvailable Commands:")
        print("-------------------")
        print("Start AI Workspace")
        return

    orchestrator = Orchestrator()
    orchestrator.execute(command)


if __name__ == "__main__":
    main()