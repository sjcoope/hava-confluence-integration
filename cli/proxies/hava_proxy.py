from typing import List
import requests
import config
from tqdm import tqdm
from cli.utils import utils, simple_cache
from cli.entities.hava_source import HavaSources
from cli.entities.hava_environment import HavaEnvironment

envs_cache = []
env_cache = dict()

def get_sources():
    resp = requests.get(config.hava["api"].format(resource = "sources"), auth=(config.hava["username"], config.hava["password"]))
    handled_response = utils.handle_response(resp)
    return HavaSources(handled_response)

# Due to the structure of the Hava API this implementation isn't optimal.  We have to get all environments, filter on the required source and then get each environment again
# as the direct call to GET/env returns more data.
def get_envs_by_source(source_id):
    result = []

    # Hit API for results and cache the results for subsequent calls in the same session.
    if len(envs_cache) == 0:
        resp = requests.get(config.hava["api"].format(resource = "environments?limit=1000"), auth=(config.hava["username"], config.hava["password"]))
        handled_response = utils.handle_response(resp)["results"]
        utils.append_to_array(envs_cache, handled_response)

    for env in tqdm(envs_cache):
        for sc in env["sources"]:
            if(sc["id"] == source_id):
                result.append(get_env(env["id"]))

    return result

def get_env(id):
    if(id not in env_cache):
        resp = requests.get(config.hava["api"].format(resource = "environments/" + id), auth=(config.hava["username"], config.hava["password"]))
        handled_response = utils.handle_response(resp)
        env =  HavaEnvironment(handled_response)
        env_cache[env.id] = env
    
    return env_cache[env.id]
