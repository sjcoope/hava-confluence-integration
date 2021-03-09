import re

def get_hava_data(key, text):
    # Expects format of [{key}]{value}[/{key}]
    regex = '\[' + key + '\](.*?)\[\/' + key + '\]'
    result = re.search(regex, text)
    if result:
        return result.group(1).strip()
    else:
        return None

