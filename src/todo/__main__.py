"""
Entry point for the Todo CLI application.
"""

from .cli.interface import TodoCLIInterface


def main() -> None:
    """Main entry point for the application."""
    cli = TodoCLIInterface()
    cli.run()


if __name__ == "__main__":
    main()