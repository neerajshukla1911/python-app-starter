import click


cli = click.Group()

from app.cli import *

if __name__ == '__main__':
    cli()