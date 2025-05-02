import json

def input_json(data):
    with open(data, 'r') as file:
        parsed_data = json.load(file)
        return parsed_data


file1 = input_json('../inputs/file1.json')
file2 = input_json('../inputs/file2.json')

print(file1)
print(file2)