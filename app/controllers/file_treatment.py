from openpyxl import load_workbook

def file_treatment(file, treatment, value_line):
    try:
        wb = load_workbook(file.path)
        sheet = wb.active

        def define_row_with_value():
            if treatment == 'automatic':
                best_match_row = None
                best_match_value = None
                
                for row in sheet.iter_rows():
                    for cell in row:
                        if cell.value is not None:
                            if best_match_row is None or cell.row < best_match_row:
                                best_match_row = cell.row
                                best_match_value = cell.value
                                break
                return best_match_value, best_match_row
            else:
                return value_line

        row_with_value = define_row_with_value()
        cell_row = row_with_value[1]

        title_row_values = sheet[cell_row]
        column_names = [cell.value for cell in title_row_values]

        wb.close()

        return column_names, wb.sheetnames
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
        cell_row = row_with_value[1]

        title_row_values = sheet[cell_row]
        column_names = [cell.value for cell in title_row_values]

        wb.close()

        return column_names
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None
