import json

def remove_column_from_json(file_path, column_to_remove):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {"Columns": []}
    
    if column_to_remove in data["Columns"]:
        data["Columns"].remove(column_to_remove)
    
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)