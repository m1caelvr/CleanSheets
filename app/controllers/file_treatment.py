import flet as ft
from openpyxl import load_workbook

def file_treatment(file):
    title_row = 1

    try:
        wb = load_workbook(file.path)
        sheet = wb.active

        def define_row_with_value():
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value is not None:
                        return cell.value, cell.row

        row_with_value = define_row_with_value()
        cell_value = row_with_value[0]
        cell_row = row_with_value[1]

        print(f'row with value: {cell_row}')

        title_row_values = sheet[cell_row]
        column_names = [cell.value for cell in title_row_values]

        num_cols = sheet.max_column
        print(f'Número de colunas na planilha: {num_cols}')

        wb.close()

        return column_names, num_cols, wb.sheetnames
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None, None

def get_columns_from_sheet(file, sheet_name):
    try:
        wb = load_workbook(file.path)
        sheet = wb[sheet_name]

        def define_row_with_value():
            for row in sheet.iter_rows():
                for cell in row:
                    if cell.value is not None:
                        return cell.value, cell.row

        row_with_value = define_row_with_value()
        cell_value = row_with_value[0]
        cell_row = row_with_value[1]

        print(f'row with value: {cell_row}')

        title_row_values = sheet[cell_row]
        column_names = [cell.value for cell in title_row_values]

        wb.close()

        return column_names
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None
