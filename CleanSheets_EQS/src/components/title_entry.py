# title_entry.py

from tkinter import Entry, Button, messagebox
from .settings import colunas_desejadas

def show_title_entry(frame, adicionar_coluna_callback):
    novo_titulo_entry = Entry(frame, bg='#fafafa')
    novo_titulo_entry.grid(row=3+len(colunas_desejadas), column=0, padx=10, pady=5, sticky='w')

    def adicionar_coluna():
        novo_titulo = novo_titulo_entry.get()
        if novo_titulo:
            colunas_desejadas.append(novo_titulo)
            messagebox.showinfo("Sucesso", f'Coluna "{novo_titulo}" adicionada.')
            adicionar_coluna_callback()
        else:
            messagebox.showwarning("Aviso", "Por favor, digite um título para adicionar.")

    btn_adicionar = Button(frame, text="Adicionar", bg='#4CAF50', fg='#fafafa', relief='flat',
                          command=adicionar_coluna)
    btn_adicionar.grid(row=3+len(colunas_desejadas), column=1, padx=(0, 10), pady=5, sticky='e')
