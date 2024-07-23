import json
import os
from pathlib import Path
from app.utils.get_path_json import get_path_json
from app.utils.get_data_json import load_json_data

def create_file_to_export(presets_to_export):
    presets_data = load_json_data()

    filtered_presets = {preset: presets_data[preset] for preset in presets_to_export if preset in presets_data}

    downloads_path = Path.home() / 'Downloads'
    export_file_path = downloads_path / 'EXPORTED_PRESETS.json'

    with open(export_file_path, 'w') as export_file:
        json.dump(filtered_presets, export_file, indent=4)

    print(f'Arquivo JSON exportado com sucesso para: {export_file_path}')