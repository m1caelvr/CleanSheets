import json

def add_column_to_json(file_path, preset_name, new_column):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {preset_name: {"Columns": []}}
    
    if preset_name not in data:
        data[preset_name] = {"Columns": []}
    
    if new_column not in data[preset_name]["Columns"]:
        data[preset_name]["Columns"].append(new_column)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)