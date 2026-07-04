# Changelog

## 2026-07-04

### Added
- Professional CLI using argparse.
- Support for CLI subcommands.
- Initial `workspace` command.
- New `app/cli` package for command handlers.

### Changed
- Replaced manual command parsing with argparse.
- Refactored CLI architecture to support one file per command.

### Removed
- Legacy `commands.py` implementation.

## Unreleased

### Added

- Installable CLI entry point (`anuragos`)
- Python packaging using Hatchling

### Changed

- Project is now executable through `uv run anuragos`

## Unreleased

### Added

- Command-line argument support
- `help` command
- Centralized logging

### Changed

- Replaced `print()` with structured logging in the Orchestrator
- Replaced `print()` with structured logging in WorkspaceAgent
- Replaced `print()` with structured logging in MacTools

## v0.1.0 - Foundation

### Added

- Project structure
- Git repository
- Python backend using uv
- Orchestrator
- Workspace Agent
- MacTools
- Agent Registry
- Configuration module

### Working Features

- Launch AI Workspace