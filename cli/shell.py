from manage import cli


@cli.command()
def shell():
    """launches shell"""
    import IPython
    IPython.embed()