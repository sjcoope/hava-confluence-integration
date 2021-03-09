
import click
from cli.commands import confluence, hava

@click.group()
def main():
    """
    Simple CLI for Hava, Confluence and integrating the two.
    """
    pass

main.add_command(confluence.conf)
main.add_command(hava.hava)