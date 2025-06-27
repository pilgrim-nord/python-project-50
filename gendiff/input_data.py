import json
from pathlib import Path

import yaml


def input_data(path_file):
    ext = Path(path_file).suffix.lower()

    with open(path_file, "r") as file:
        if ext == ".yaml" or ext == ".yml":
            return yaml.safe_load(file)
        elif ext == ".json":
            return json.load(file)
        else:
            raise ValueError(f"Неподдерживаемый формат файла: {ext}")


