import os
import json

default_columns = {
    "preset_1": {
        "Columns": [
            "N_OS",
            "Data_Hora_Abertura",
            "Denominacao_Site",
            "UF",
            "Descricao_Tipo_Servico",
            "Denominacao_Prioridade",
            "Descricao_OS",
            "Textos_OS",
            "Denominacao_Estado_OS",
            "Data_Hora_Faturamento"
        ]
    }
}

def create_json_file(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as json_file:
            json.dump(default_columns, json_file, indent=4)
        print(f'Arquivo JSON criado em {file_path}')
    else:
        print('O arquivo JSON já existe')