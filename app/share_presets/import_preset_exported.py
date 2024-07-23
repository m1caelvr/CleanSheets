import json
from app.utils.get_path_json import get_path_json

def import_preset_exported(file_path):
    if not file_path.endswith('.json'):
        feedback_mensage = 'Erro: O arquivo selecionado não é um arquivo JSON.'
        return feedback_mensage

    existn_json_path = get_path_json()

    with open(existn_json_path, 'r') as file:
        existing_presets = json.load(file)

    with open(file_path, 'r') as file:
        imported_presets = json.load(file)

    for preset_name, preset_data in imported_presets.items():
        new_preset_name = preset_name
        counter = 1

        while new_preset_name in existing_presets:
            new_preset_name = f"{preset_name}_{counter}"
            counter += 1

        existing_presets[new_preset_name] = preset_data

    with open(existn_json_path, 'w') as file:
        json.dump(existing_presets, file, indent=4)

    feedback_mensage = 'Presets importados com sucesso!'
    return feedback_mensage