import json
from app.utils.get_path_json import get_path_json

def remove_column_from_json(preset_name, column_to_remove):
    file_path = get_path_json()
    
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {preset_name: {"Columns": []}}
    
    if preset_name in data and column_to_remove in data[preset_name]["Columns"]:
        data[preset_name]["Columns"].remove(column_to_remove)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
