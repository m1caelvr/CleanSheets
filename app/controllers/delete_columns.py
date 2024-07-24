import openpyxl as op

def delete_columns(file_path, sheet_name, columns_to_remove):
    if not columns_to_remove:
        print("Nenhuma coluna selecionada para deletar.")
        return
    
    print(f"Deletando colunas {', '.join(map(str, columns_to_remove))} do arquivo {file_path} na planilha {sheet_name}")
    
    try:
        workbook = op.load_workbook(filename=file_path)
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return
    except PermissionError:
        print(f"Erro: Sem permissão para acessar o arquivo {file_path}.")
        return
    except op.utils.exceptions.InvalidFileException:
        print(f"Erro: O arquivo {file_path} não é um arquivo Excel válido.")
        return
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return

    try:
        sheet = workbook[sheet_name]
    except KeyError:
        print(f"Erro: A planilha {sheet_name} não foi encontrada no arquivo.")
        return

    columns_to_remove.sort(reverse=True)
    
    for col in columns_to_remove:
        sheet.delete_cols(col)

    try:
        workbook.save(filename=file_path)
        print("Colunas deletadas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")