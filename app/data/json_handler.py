from app.utils.create_file import create_json_file
from app.utils.get_path_json import get_path_json
from app.utils.get_data_json import load_json_data
from app.utils.save_data_json import save_json_data

def ensure_documents_json_file():
    json_file_path = get_path_json()
    create_json_file(json_file_path)
    
    return json_file_path