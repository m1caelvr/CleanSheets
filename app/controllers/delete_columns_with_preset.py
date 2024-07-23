import pandas as pd
from app.utils.get_data_json import load_json_data

def delete_columns_with_preset(path, sheet, preset_name, keeps):
    print(f'Keep value: {keeps}')

    try:
        presets = load_json_data()
        
        if preset_name not in presets:
            print(f"Preset '{preset_name}' não encontrado no JSON.")
            return f"Preset '{preset_name}' não encontrado no JSON.", [], ""
        
        preset_data = presets[preset_name]
        preset_columns = set(preset_data.get('Columns', []))
        
        if not preset_columns:
            print(f"Nenhuma coluna especificada para o preset '{preset_name}'.")
            return f"Nenhuma coluna especificada para o preset '{preset_name}'.", [], ""
        
        df = pd.read_excel(path, sheet_name=sheet)

        cols_to_remove = []
        cols_not_found = [] 
        for col in df.columns:
            found_in_preset = False
            not_found_values = []
            
            for value in df[col].head(10).unique():
                if value in preset_columns:
                    found_in_preset = True
                    break
                else:
                    not_found_values.append(value)
            
            if keeps == 'true':
                if not found_in_preset:
                    cols_to_remove.append(col)
                else:
                    cols_not_found.append((col, not_found_values))
            else:
                if found_in_preset:
                    cols_to_remove.append(col)
                else:
                    cols_not_found.append((col, not_found_values))
                
        if not cols_to_remove:
            action = 'manter' if keeps == 'true' else 'deletar'
            print(f"Nenhuma coluna encontrada para {action} no preset '{preset_name}'.")
            return f"Nenhuma coluna encontrada para {action} no preset '{preset_name}'.", [], ""

        remaining_columns = [col for col in df.columns if col not in cols_to_remove]
        chunk_size = 10000
        writer = pd.ExcelWriter(path, engine='openpyxl', mode='a', if_sheet_exists='replace')

        for start_row in range(0, len(df), chunk_size):
            df_chunk = df.iloc[start_row:start_row + chunk_size, :][remaining_columns]
            if start_row == 0:
                df_chunk.to_excel(writer, sheet_name=sheet, index=False)
        
        writer.close()
        
        action = 'mantidas' if keeps == True else 'deletadas'
        print(f"{len(cols_to_remove)} Colunas {action} com sucesso do arquivo {path} na planilha {sheet}.")
        status_msg = f"Colunas {action} com sucesso do arquivo {path} na planilha {sheet}."
        found_msg = f"Foram {action} {len(cols_to_remove)} colunas de {len(preset_columns)} presentes no JSON."
        return status_msg, list(cols_to_remove), found_msg

    except Exception as e:
        print(f"Erro ao processar: {e}")
        return f"Erro ao processar: {e}", [], ""
