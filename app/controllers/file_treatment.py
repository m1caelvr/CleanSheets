from openpyxl import load_workbook

def file_treatment(file):
    try:
        wb = load_workbook(file.path)
        sheet = wb.active
        cell_value = sheet['A1'].value
        print(f'Valor da célula A1: {cell_value}')

        num_cols = sheet.max_column
        print(f'Número de colunas na planilha: {num_cols}')

        wb.close()

        return cell_value, num_cols
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None, None