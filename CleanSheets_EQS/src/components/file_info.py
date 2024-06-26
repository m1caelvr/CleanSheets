# file_info.py

from tkinter import Label

def show_file_info(frame, file_name, novo_nome):
    Label(frame, text="Nome do Arquivo:", bg='#050505', fg='#fafafa').grid(row=0, column=0, sticky='w')
    Label(frame, text=file_name, bg='#050505', fg='#fafafa').grid(row=0, column=1, sticky='w')

    Label(frame, text="Nome do Arquivo Final:", bg='#050505', fg='#fafafa').grid(row=1, column=0, sticky='w')
    Label(frame, text=novo_nome, bg='#050505', fg='#fafafa').grid(row=1, column=1, sticky='w')
