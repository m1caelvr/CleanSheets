import os
import platform
import subprocess

def open_documents_folder():
    home = os.path.expanduser("~")
    documents_folder = os.path.join(home, "Documents")
    
    os.makedirs(documents_folder, exist_ok=True)
    
    json_file_path = os.path.join(documents_folder, "CLEANSHETS_DATA.json")
    
    if not os.path.exists(json_file_path):
        with open(json_file_path, 'w') as json_file:
            json_file.write('{}')

    if platform.system() == "Windows":
        os.startfile(documents_folder)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", documents_folder])
    else: 
        subprocess.Popen(["xdg-open", documents_folder])

if __name__ == "__main__":
    open_documents_folder()