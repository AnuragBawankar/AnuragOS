import argparse

from app.cli.workspace import workspace_command


def main():

    parser = argparse.ArgumentParser(
        prog="anuragos",
        description="AnuragOS - AI Operating System",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    workspace_parser = subparsers.add_parser(
        "workspace",
        help="Start AI Workspace",
    )

    workspace_parser.set_defaults(func=workspace_command)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()