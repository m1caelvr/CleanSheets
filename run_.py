import tkinter as tk
from tkinter import messagebox

# Função que será chamada quando um dos radio buttons for selecionado
def on_radio_select():
    selected_option = radio_var.get()
    if selected_option:
        print(f"Selecionado: {selected_option}")

# Criando a janela principal
root = tk.Tk()
root.title("Você deseja:")

# Variável para armazenar a opção selecionada
radio_var = tk.StringVar()

# Criando o título
title_label = tk.Label(root, text="Você deseja:")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Criando os radio buttons
radio_excluir = tk.Radiobutton(root, text="Excluir", variable=radio_var, value="excluir", command=on_radio_select)
radio_excluir.grid(row=1, column=0, padx=20, pady=10)

radio_manter = tk.Radiobutton(root, text="Manter", variable=radio_var, value="manter", command=on_radio_select)
radio_manter.grid(row=1, column=1, padx=20, pady=10)

# Iniciando o loop da interface gráfica
root.mainloop()
