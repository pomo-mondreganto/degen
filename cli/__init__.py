import click

from .generate import generate


@click.group()
def cli():
    pass


cli: click.Group  # noqa
cli.add_command(generate)
