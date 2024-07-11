import os
import json

def load_json_data(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data
