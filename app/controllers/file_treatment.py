from openpyxl import load_workbook

def file_treatment(file):
    try:
        wb = load_workbook(file.path)
        sheetnames = wb.sheetnames
        column_counts = {sheet: wb[sheet].max_column for sheet in sheetnames}
        wb.close()
        return sheetnames, column_counts
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None, None

def get_columns_from_sheet(file, sheet_name, treatment, specified):
    try:
        wb = load_workbook(file.path)
        sheet = wb[sheet_name]

        if treatment == 'automatic':
            column_names = []
            max_rows = sheet.max_row if sheet.max_row < 10 else 10
            
            for col in sheet.iter_cols(min_row=1, max_row=max_rows):
                column_name = None
                for cell in col:
                    if cell.value is not None:
                        column_name = cell.value
                        break
                column_names.append(column_name)
        else:
            column_names = [cell.value for cell in sheet[specified]]

        wb.close()

        # print(column_names)
        return column_names
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None
