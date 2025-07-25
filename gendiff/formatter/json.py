import json as json_module


def json(diff):
    return json_module.dumps(diff, indent=4)