import json

def add_column_to_json(file_path, new_column):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"Columns": []}
    
    if new_column not in data["Columns"]:
        data["Columns"].append(new_column)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)