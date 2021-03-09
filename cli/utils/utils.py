import jsonpickle

def to_json(array):
    return jsonpickle.encode(array, unpicklable=False, indent=4)

def handle_response(resp):
    if(resp.status_code != 200):
        raise RuntimeError(resp.status_code + ": " + resp.text)

    return resp.json()