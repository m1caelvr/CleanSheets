# src/filter.py

import pandas as pd
from tkinter import Tk, filedialog
import os

def selecionar_arquivo():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo Excel",
        filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
    )
    return file_path
