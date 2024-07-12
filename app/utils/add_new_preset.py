import json
from app.utils.get_path_json import get_path_json
from app.utils.get_presets_names import get_presets_names

def add_new_preset():
    file_path = get_path_json()

    data = get_presets_names()
    
    max_index = 0
    for key in data.keys():
        if key.startswith("preset_"):
            try:
                index = int(key.split("_")[1])
                if index > max_index:
                    max_index = index
            except ValueError:
                continue
    
    new_preset_name = f"preset_{max_index + 1}"
    
    data[new_preset_name] = {"Columns": []}
    
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f'Novo preset adicionado: {new_preset_name}')