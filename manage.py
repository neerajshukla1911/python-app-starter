import click


cli = click.Group()

from cli import *

if __name__ == '__main__':
    cli()