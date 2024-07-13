import json
from collections import OrderedDict
from app.utils.get_path_json import get_path_json

def update_preset_in_json(old_name, new_name):
    json_file_path = get_path_json()
    with open(json_file_path, 'r') as file:
        data = json.load(file, object_pairs_hook=OrderedDict)
        
    if new_name in data:
        print(f"O novo nome '{new_name}' já existe no JSON.")
        return
    
    if old_name in data:
        new_data = OrderedDict()
        
        for key, value in data.items():
            if key == old_name:
                new_data[new_name] = value
            else:
                new_data[key] = value
        
        with open(json_file_path, 'w') as file:
            json.dump(new_data, file, indent=4)
        
        print(f"Preset '{old_name}' atualizado para '{new_name}' no JSON.")
    else:
        print(f"Preset '{old_name}' não encontrado no JSON.")
