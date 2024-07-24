import os
import requests
import webbrowser

def check_for_update():
    remote_version_url = "https://raw.githubusercontent.com/m1caelvr/CleanSheets/main/version.txt"
    local_version_file = "version.txt"
    
    try:
        # if not os.path.exists(local_version_file):
        #     local_version = "0.0.0"
        # else:
        #     with open(local_version_file, "r") as f:
        #         local_version = f.read().strip()

        local_version = "0.1.1"

        response = requests.get(remote_version_url)
        remote_version = response.text.strip()

        if remote_version > local_version:
            print("Nova atualização disponível!")
            new_version = True
            return new_version, local_version, remote_version
        else:
            print("Você já está na versão mais recente.")
            new_version = False
            return new_version, local_version, remote_version
    
    except Exception as e:
        print(f"Erro ao verificar atualização: {e}")
        return f"Erro ao verificar atualização: {e}"


def download_and_apply_update():
    try:
        remote_version_url = "https://raw.githubusercontent.com/m1caelvr/CleanSheets/main/version.txt"
        response = requests.get(remote_version_url)
        remote_version = response.text.strip()

        update_url = f"https://github.com/m1caelvr/CleanSheets/releases/download/v{remote_version}/Cleansheets.exe"

        webbrowser.open(update_url)
    
    except Exception as e:
        print(f"Erro ao aplicar atualização: {e}")


