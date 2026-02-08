import json
from pathlib import Path


def load_config():
    with open("config.json") as f:
        config = json.load(f)

    watch_folder = Path.home() / config["watch_folder"]
    categories = config["categories"]
    remove_duplicates = config["remove_duplicates"]

    return watch_folder, categories, remove_duplicates
