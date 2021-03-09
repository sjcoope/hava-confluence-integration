import json
import jsonpickle

def serialise_to_json(array):
    return jsonpickle.encode(array, unpicklable=False, indent=4)

def output_as_json(input):
    return json.dumps(input, indent=4, sort_keys=True)

def handle_response(resp):
    if(resp.status_code != 200):
        raise RuntimeError(str(resp.status_code) + ": " + resp.text)

    return resp.json()

def append_to_array(array, source_array):
    for item in source_array:
        array.append(item)