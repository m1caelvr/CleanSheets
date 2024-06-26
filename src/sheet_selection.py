# src/sheet_selection.py

import tkinter as tk
from tkinter import ttk

def select_sheet(workbook):
    sheet_names = workbook.sheetnames

    def on_select():
        selected_sheet.set(sheet_name_var.get())
        sheet_window.quit()

    sheet_window = tk.Tk()
    sheet_window.title("Selecione a Planilha")

    sheet_name_var = tk.StringVar(value=sheet_names[0])
    selected_sheet = tk.StringVar()

    for name in sheet_names:
        rb = ttk.Radiobutton(sheet_window, text=name, variable=sheet_name_var, value=name)
        rb.pack(anchor=tk.W, padx=20, pady=5)

    confirm_button = ttk.Button(sheet_window, text="Confirmar", command=on_select)
    confirm_button.pack(pady=20)

    sheet_window.mainloop()
    sheet_window.destroy()

    return selected_sheet.get()