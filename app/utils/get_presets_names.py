import json
import os
from app.utils.get_path_json import get_path_json

def load_json_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data

def get_presets_names():
    file_path = get_path_json()
    data = load_json_data(file_path)
    presets_names = {key: value for key, value in data.items()}
    return presets_names