import json
from app.utils.get_path_json import get_path_json

def remove_preset_from_json(preset_name):
    json_file_path = get_path_json()
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    if preset_name in data:
        del data[preset_name]
    else:
        print(f"Preset '{preset_name}' não encontrado no JSON.")

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print("JSON atualizado com sucesso.")