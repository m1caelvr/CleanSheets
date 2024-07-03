def delete_columns(file, sheet, columns):
    if not columns:
        print("Nenhuma coluna selecionada para deletar.")
        return
    
    print(f"Deletando colunas {'\n'.join(columns)} do arquivo {file} na planilha {sheet}")
