import json


def input_data(data):
    with open(data, "r") as file:
        parsed_data = json.load(file)
        return parsed_data


