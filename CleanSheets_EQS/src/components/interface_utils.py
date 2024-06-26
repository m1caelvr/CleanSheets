# interface_utils.py

import os

def get_file_info(file_path):
    dir_name = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    novo_nome = f"{name}-resumo{ext}"
    return base_name, novo_nome
