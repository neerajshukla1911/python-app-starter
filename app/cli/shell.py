from aioconsole import events

from manage import cli


@cli.command()
def shell():
    """launches shell"""
    events.run_console()
