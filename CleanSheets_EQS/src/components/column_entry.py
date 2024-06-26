# column_entry.py

from tkinter import Label, Button, messagebox
from .settings import colunas_desejadas

def show_columns(frame, remover_coluna_callback):
    for i, coluna in enumerate(colunas_desejadas):
        label = Label(frame, text=coluna, bg='#1f1f1f', fg='#fafafa', padx=5, pady=5, borderwidth=0, relief="flat",
                      width=15, height=2, bd=0, font=("Arial", 12))
        label.grid(row=3+i, column=0, padx=10, pady=5, sticky='w')

        btn_remover = Button(frame, text="X", bg='#ff4d4d', fg='#fafafa', relief='flat',
                            command=lambda col=coluna: remover_coluna_callback(col))
        btn_remover.grid(row=3+i, column=1, padx=(0, 10), pady=5, sticky='e')
