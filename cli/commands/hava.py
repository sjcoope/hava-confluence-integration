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

@hava.command("get-source")
@click.option("-i", "--id", help="The id of the source to retrieve")
def cmd_get_source(id):
    print('Getting source from Hava.')
    source = hava_proxy.get_source(id)
    results_for_output = utils.serialise_to_json(source)
    print(results_for_output)

@hava.command("get-env")
@click.option("-i", "--id")
def cmd_get_env(id):
    print('Getting environment with id "{id}" from Hava.'.format(id = id))
    env = hava_proxy.get_env(id)

    results_for_output = utils.serialise_to_json(env)
    print(results_for_output)

@hava.command("get-stats")
@click.option("-s", "--source", help="The source to get stats for.")
def hv_get_stats(source):
    
    stats = dict(
        sources=0,
        envs=0
    )

    envs = []
    if(source):
        print('getting stats for source "{source}" from hava...'.format(source = source))
        stats["sources"] = 1
        envs = hava_proxy.get_env_count_by_source(source)
    else:
        print("getting stats of all hava resources...")
        for source in hava_proxy.get_sources():
            stats["sources"] += 1
        envs = hava_proxy.get_envs()

    for env in envs:
        stats["envs"] += 1

    print(utils.serialise_to_json(stats))