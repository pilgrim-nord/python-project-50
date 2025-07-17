import json


def json(diff) -> str:
    return json.dumps(diff, indent=4)