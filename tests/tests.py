# src/file_operations.py

from openpyxl import load_workbook

def remove_columns(file_path, sheet_name, columns_to_remove):
    workbook = load_workbook(filename=file_path)
    sheet = workbook[sheet_name]
    columns_to_remove.sort(reverse=True)

    for col in columns_to_remove:
        sheet.delete_cols(col)

    workbook.save(filename=file_path)
    
# remove_columns(file_path, sheet_name, columns_to_remove)
