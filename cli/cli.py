import click
from cli.commands.confluence import conf

@click.group()
def main():
    """
    Simple CLI for Hava, Confluence and integrating the two.
    """
    pass

main.add_command(conf)