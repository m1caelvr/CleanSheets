import tkinter as tk
from tkinter import ttk, messagebox
import logging

# Configuração básica do logger
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

    def confirm_selection():
        logging.info(f"Operação selecionada: {selected_operation}")  # Log da operação selecionada
        if selected_operation == "excluir":
            return columns_to_remove
        elif selected_operation == "manter":
            all_columns = set(range(1, sheet.max_column + 1))
            columns_to_keep = list(all_columns - set(columns_to_remove))
            return columns_to_keep

    def on_operation_change():
        global selected_operation
        selected_operation = operation_var.get()
        logging.info(f"Operação alterada para: {selected_operation}")  # Log da mudança de operação

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

    # Opções de Excluir ou Manter
    global selected_operation
    operation_var = tk.StringVar()  # Não define um valor inicial aqui
    selected_operation = "excluir"  # Valor inicial padrão
    ttk.Radiobutton(columns_window, text="Excluir", variable=operation_var, value="excluir", command=on_operation_change).grid(row=4, column=0, padx=20, pady=5, sticky=tk.W)
    ttk.Radiobutton(columns_window, text="Manter", variable=operation_var, value="manter", command=on_operation_change).grid(row=5, column=0, padx=20, pady=5, sticky=tk.W)

    # Exibição dos valores adicionados em linha
    textbox_label = ttk.Label(columns_window, text="Colunas Selecionadas:")
    textbox_label.grid(row=6, column=0, padx=20, pady=5, sticky=tk.W)

    textbox = tk.Text(columns_window, height=1, width=20, wrap=tk.NONE)
    textbox.grid(row=7, column=0, padx=20, pady=5, sticky=tk.W+tk.E)

    update_textbox()

    confirm_button = ttk.Button(columns_window, text="Confirmar", command=lambda: columns_window.quit())
    confirm_button.grid(row=8, columnspan=3, pady=5)

    columns_window.mainloop()
    columns_window.destroy()

    # Retorna as colunas a serem removidas ou mantidas baseado na escolha do usuário
    return confirm_selection()
