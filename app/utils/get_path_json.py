import os

def get_path_documents():
    home = os.path.expanduser("~")
    documents_folder = os.path.join(home, "Documents")
    return documents_folder

def get_path_json():
    documents_folder = get_path_documents()
    os.makedirs(documents_folder, exist_ok=True)
    json_file_path = os.path.join(documents_folder, 'CLEANSHETS_DATA.json')

    return json_file_path