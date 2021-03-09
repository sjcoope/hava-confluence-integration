import click
from tqdm import tqdm
from cli.proxies import hava_proxy
from cli.utils import utils

@click.group()
def hava():
    """
    Hava specific commands and operations.
    """
    pass

@hava.command("list-sources")
@click.option("-e", "--environments", default="n", help="If set the list of sources will also load all environments")
def cmd_list_sources(environments):
    print('Listing sources from Hava.')
    sources = hava_proxy.get_sources()

    if environments == 'y':
        for source in tqdm(sources):
            print('Getting environments for source with id "{id}" from Hava.'.format(id = source.id))
            source.environments = hava_proxy.get_envs_by_source(source.id)

    results_for_output = utils.serialise_to_json(sources)
    print(results_for_output)

@hava.command("get-env")
@click.option("-i", "--id")
def cmd_get_env(id):
    print('Getting environment with id "{id}" from Hava.'.format(id = id))
    env = hava_proxy.get_env(id)

    results_for_output = utils.serialise_to_json(env)
    print(results_for_output)