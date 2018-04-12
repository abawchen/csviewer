from .client import ViewerClient

def cli():
    """Creates and calls ViewerClient."""
    client = ViewerClient()
    client.cli()

if __name__ == "__main__":
    cli()
