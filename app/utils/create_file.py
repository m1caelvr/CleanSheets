import os
import json

default_columns = {
    "Preset_1": {
        "Columns": []
    }
}

def create_json_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump(default_columns, json_file, indent=4)
        print(f'Arquivo JSON criado em {file_path}')
    else:
        print('O arquivo JSON já existe')