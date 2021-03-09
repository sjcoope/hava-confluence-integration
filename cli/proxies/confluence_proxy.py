
from typing import List
import requests
import config
from cli.utils import utils
from cli.entities.confluence_pages import ConfluencePages

# TODO:
# - Error handling

def get_content_by_space(space_key):
    resp = requests.get(
        config.confluence["api"].format(resource = "content"), 
        params={"spaceKey": space_key, "type": "page", "status": "current", "limit": config.confluence["limit"]}, 
        auth=(config.confluence["username"], config.confluence["password"]))  

    handled_response = utils.handle_response(resp)
    return ConfluencePages(handled_response["results"])

def get_content_children(content_id):
    resp = requests.get(
        config.confluence["api"].format(resource = "content/{id}/child".format(id=content_id)),
        params={"expand": "page", "orderby": "title asc", "limit": 500},
        auth=(config.confluence["username"], config.confluence["password"]))

    handled_response = utils.handle_response(resp)
    return ConfluencePages(handled_response["page"]["results"])
    
def get_content_body(content_id):
    resp = requests.get(
        config.confluence["api"].format(resource = "content/{id}?expand=page,body.storage".format(id=content_id)),
        params={"expand": "page", "orderby": "title asc", "limit": 500},
        auth=(config.confluence["username"], config.confluence["password"]))

    handled_response = utils.handle_response(resp)
    return handled_response["body"]["storage"]["value"]