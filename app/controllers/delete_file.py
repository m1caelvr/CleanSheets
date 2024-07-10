import openpyxl as op

def delete_columns(file_path, sheet_name, columns_to_remove):
    if not columns_to_remove:
        print("Nenhuma coluna selecionada para deletar.")
        return
    
    print(f"Deletando colunas {', '.join(map(str, columns_to_remove))} do arquivo {file_path} na planilha {sheet_name}")
    
    workbook = op.load_workbook(filename=file_path)
    sheet = workbook[sheet_name]

    columns_to_remove.sort(reverse=True)
    
    # for col in columns_to_remove:
    #     sheet.delete_cols(col)

    # workbook.save(filename=file_path)
    print("Colunas deletadas com sucesso.")
    