from manage import cli
import click
from app import sanic_app
import asyncio

loop = asyncio.get_event_loop()

@cli.command()
@click.option('--host', default="0.0.0.0", help='host name/ip address')
@click.option('--port', type=int, default=8000, help='Port on which server to run')
@click.option('--workers', type=int, default=1, help='No of workers')
@click.option('--debug', type=bool, default=True, help='Debug flag')
def run(host, port, workers, debug):
    """Runs sanic server"""
    sanic_app.run(host=host, port=port, workers=workers, debug=debug, loop=loop)