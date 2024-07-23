import json
from app.utils.get_path_json import get_path_json
from app.utils.get_presets_names import get_presets_names

def import_preset_exported(file_path):
    # Carregar o caminho do arquivo JSON existente
    existn_json_path = get_path_json()

    # Carregar os dados do arquivo JSON existente
    with open(existn_json_path, 'r') as file:
        existing_presets = json.load(file)

    # Carregar os dados do arquivo JSON importado
    with open(file_path, 'r') as file:
        imported_presets = json.load(file)

    # Iterar sobre os presets importados
    for preset_name, preset_data in imported_presets.items():
        new_preset_name = preset_name
        counter = 1

        # Verificar se o preset já existe no arquivo existente
        while new_preset_name in existing_presets:
            new_preset_name = f"{preset_name}_{counter}"
            counter += 1

        # Adicionar o preset com o novo nome (se necessário) ao arquivo existente
        existing_presets[new_preset_name] = preset_data

    # Salvar o arquivo JSON atualizado
    with open(existn_json_path, 'w') as file:
        json.dump(existing_presets, file, indent=4)

    print(f'Presets importados com sucesso e salvos em: {existn_json_path}')