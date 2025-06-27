import yaml
import json


with open("file1.yaml", "r") as file:
    data = yaml.safe_load(file)
    print(data)

with open("file1.json", "r") as file:
    parsed_data = json.load(file)
    print(parsed_data)


