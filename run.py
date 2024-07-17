import flet as ft
from app.main import main
import requests
import os

def check_for_update():
    remote_version_url = "https://raw.githubusercontent.com/m1caelvr/CleanSheets-Flet/main/version.txt"
    local_version_file = "version.txt"
    
    try:
        if not os.path.exists(local_version_file):
            local_version = "0.0.0"
        else:
            with open(local_version_file, "r") as f:
                local_version = f.read().strip()

        response = requests.get(remote_version_url)
        remote_version = response.text.strip()

        if remote_version > local_version:
            print("Nova atualização disponível!")
            download_and_apply_update(remote_version)
        else:
            print("Você já está na versão mais recente.")
            start_application()
    
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")
        start_application()

def download_and_apply_update(remote_version):
    update_url = f"https://github.com/seu-usuario/cleansheets/releases/download/v{remote_version}/seu_app.exe"
    temp_filename = "novo_executavel.exe"
    local_version_file = "version.txt"

    try:
        # response = requests.get(update_url, stream=True)
        # with open(temp_filename, 'wb') as f:
        #     for chunk in response.iter_content(chunk_size=8192):
        #         f.write(chunk)

        print("Atualização baixada com sucesso!")

        os.replace(temp_filename, "seu_app.exe")
        
        with open(local_version_file, "w") as f:
            f.write(remote_version)

        print("Atualização aplicada com sucesso!")
        start_application()
    
    except Exception as e:
        print(f"Erro ao aplicar atualização: {e}")
        start_application()

def start_application():
    print("Iniciando o aplicativo...")
    ft.app(target=main)

check_for_update()