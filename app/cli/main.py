import click

from .viewer import Viewer

def cli():
    """Creates and calls Viewer"""
    try:
        viewer = Viewer()
        viewer.run_cli()
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    cli()
