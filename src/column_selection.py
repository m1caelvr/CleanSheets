import tkinter as tk
from tkinter import ttk, messagebox
import logging

logging.basicConfig(level=logging.INFO)

def select_columns(sheet, columns_to_remove):
    def add_custom_column():
        try:
            column_number = int(custom_column_entry.get())
            if column_number <= 0:
                raise ValueError("Insira um número inteiro positivo.")
            
            columns_to_remove.append(column_number)
            custom_column_entry.delete(0, tk.END)
            update_textbox()
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def update_textbox():
        textbox.delete(1.0, tk.END)
        columns_text = ' '.join(map(str, columns_to_remove))
        textbox.insert(tk.END, columns_text)

    columns_to_remove_value = []
    clicked = False

    def confirm_selection(value):
        nonlocal columns_to_remove_value
        nonlocal clicked

        logging.info(f"Opção selecionada: {value}")

        if not value:
            messagebox.showerror("Erro", "Selecione uma opção: Excluir ou Manter.")
            return None

        if value == "excluir":
            columns_to_remove_value = columns_to_remove[:]
            clicked = True
        elif value == "manter":
            all_columns = set(range(1, sheet.max_column + 1))
            columns_to_keep = list(all_columns - set(columns_to_remove))
            columns_to_remove_value = columns_to_keep[:]
            clicked = True

        logging.info(f"Colunas selecionadas para {value}: {columns_to_remove_value}")
        update_textbox()

    columns_window = tk.Tk()
    columns_window.title("Selecione as Colunas para Remover")

    columns_to_remove.clear()

    # Título
    custom_column_label = ttk.Label(columns_window, text="Digite a coluna")
    custom_column_label.grid(row=0, column=0, padx=20, pady=5, sticky=tk.W)

    # Campo para inserir número da coluna personalizada
    custom_column_entry = ttk.Entry(columns_window)
    custom_column_entry.grid(row=1, column=0, padx=20, pady=5, sticky=tk.W)

    # Botão para adicionar coluna
    add_custom_column_button = ttk.Button(columns_window, text="Adicionar", command=add_custom_column)
    add_custom_column_button.grid(row=2, column=0, padx=20, pady=5, sticky=tk.W)

    ttk.Separator(columns_window, orient=tk.HORIZONTAL).grid(row=3, columnspan=3, sticky="ew", padx=20, pady=10)

    # Opções de Excluir ou Manter com Radio Buttons
    radio_var = tk.StringVar()

    radio_excluir = tk.Radiobutton(columns_window, text="Excluir", variable=radio_var, value="excluir", 
                                   command=lambda: confirm_selection("excluir"))
    radio_excluir.grid(row=4, column=0, padx=20, pady=10)

    radio_manter = tk.Radiobutton(columns_window, text="Manter", variable=radio_var, value="manter", 
                                  command=lambda: confirm_selection("manter"))
    radio_manter.grid(row=4, column=1, padx=20, pady=10)

    available_columns_label = ttk.Label(columns_window, text=f"Colunas disponíveis: {sheet.max_column}")
    available_columns_label.grid(row=5, column=0, columnspan=2, padx=20, pady=5, sticky=tk.W)

    textbox_label = ttk.Label(columns_window, text="Colunas Selecionadas:")
    textbox_label.grid(row=6, column=0, padx=20, pady=5, sticky=tk.W)

    textbox = tk.Text(columns_window, height=1, width=20, wrap=tk.NONE)
    textbox.grid(row=7, column=0, padx=20, pady=5, sticky=tk.W+tk.E)

    update_textbox()

    def on_confirm_button():
        if not clicked:
            messagebox.showerror("Erro", "Selecione uma opção: Excluir ou Manter.")
        else:
            columns_window.quit()

    confirm_button = ttk.Button(columns_window, text="Confirmar", command=on_confirm_button)
    confirm_button.grid(row=8, columnspan=3, pady=5)

    columns_window.mainloop()

    selected_columns = columns_to_remove_value
    columns_window.destroy()

    return selected_columns
