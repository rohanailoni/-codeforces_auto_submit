import json
def Load_json(filepath):
    """
    return none if the file is empty
    or parsed json in python dictionary
    """
    f = open(filepath)
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError:
        "The file is either empty or not json file"
        return None

    return data