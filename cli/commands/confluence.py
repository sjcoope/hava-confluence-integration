import click
from cli.proxies import confluence_proxy
from cli.utils import utils

#TODO - have a look at nesting commands - https://click.palletsprojects.com/en/6.x/quickstart/#nesting-commands


@click.group()
def conf():
    """
    Confluence specific commands and operations.
    """
    pass

@conf.command("list-pages")
@click.option("-s", "--space_key", help="The key of the space to list pages for.")
def cmd_list_content(space_key):
    print('Getting content for space "{space_key}"'.format(space_key=space_key))
    results = confluence_proxy.get_content_by_space(space_key)
    encoded_results = utils.to_json(results)
    print(encoded_results)

@conf.command("list-child-pages")
@click.option("-p", "--page_id", help="The id of the page to list child pages for.")
def cmd_list_children(page_id):
    print('Getting children for page with id "{page_id}"'.format(page_id=page_id))
    results = confluence_proxy.get_content_children(page_id)
    encoded_results = utils.to_json(results)
    print(encoded_results)

@conf.command("get-body")
@click.option("-p", "--page_id", help="The id of the page to get the body for.")
def cmd_get_content_body(page_id):
    print('Getting body for page with id "{page_id}"'.format(page_id=page_id))
    results = confluence_proxy.get_content_body(page_id)
    encoded_results = utils.to_json(results)
    print(encoded_results)