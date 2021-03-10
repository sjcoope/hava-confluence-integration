from typing import List
import requests
import config
from tqdm import tqdm
from cli.utils import utils
from cli.entities.hava_source import HavaSource, HavaSources
from cli.entities.hava_environment import HavaEnvironment

envs_summary_cache = []
envs_full_cache = dict()
sources_full_cache = []

# Don't make single source API call as it returns less information than getting all sources.
def get_source(id):
    if(id == None): raise ValueError('get_source expects "id" which was not supplied')
    sources = get_sources()
    for source in sources:
        if(source.id == id):
            return source

def get_sources():
    if(len(sources_full_cache) == 0):
        resp = requests.get(config.hava["api"].format(resource = "sources"), auth=(config.hava["username"], config.hava["password"]))
        handled_response = utils.handle_response(resp)
        utils.append_to_array(sources_full_cache, HavaSources(handled_response))

    return sources_full_cache

# Due to the structure of the Hava API this implementation isn't optimal.  We have to get all environments, filter on the required source and then get each environment again
# as the direct call to GET/env returns more data.
def get_envs_by_source(source_id):
    if(source_id == None): raise ValueError('get_envs_by_source expects "source_id" which was not supplied')
    result = []

    # Hit API for results and cache the results for subsequent calls in the same session.
    envs = get_envs()
    for env in tqdm(envs):
        for sc in env["sources"]:
            if(sc["id"] == source_id):
                result.append(get_env(env["id"]))

    return result

def get_env_count_by_source(source_id):
    if(source_id == None): raise ValueError('get_envs_by_source expects "source_id" which was not supplied')
    result = []

    envs = get_envs()
    for env in envs:
        for sc in env["sources"]:
            if(sc["id"] == source_id):
                result.append(env)
    
    return result

def get_envs():
    if len(envs_summary_cache) == 0:
        resp = requests.get(config.hava["api"].format(resource = "environments?limit=1000"), auth=(config.hava["username"], config.hava["password"]))
        handled_response = utils.handle_response(resp)["results"]
        utils.append_to_array(envs_summary_cache, handled_response)

    return envs_summary_cache

def get_env(id):
    if(id == None): raise ValueError('get_env expects "id" which was not supplied')

    if(id not in envs_full_cache):
        resp = requests.get(config.hava["api"].format(resource = "environments/" + id), auth=(config.hava["username"], config.hava["password"]))
        handled_response = utils.handle_response(resp)
        env =  HavaEnvironment(handled_response)
        envs_full_cache[env.id] = env
    
    return envs_full_cache[env.id]

def get_env_share_by_revision(environment_id, revision_id):
    account_id = config.hava["account_id"]
    url = config.hava["api"].format(resource = "environments/" + environment_id + "/share?account_id=" + account_id + "&revision_id=" + str(revision_id))
    resp = requests.get(url, auth=(config.hava["username"], config.hava["password"]))
    return utils.handle_response(resp)
