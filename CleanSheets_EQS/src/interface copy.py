# interface.py

import pandas as pd
from tkinter import Tk, filedialog, Label, Entry, Button, Frame, messagebox
import os

# Configurações iniciais
colunas_desejadas = ['Coluna1', 'Coluna2', 'Coluna3']
lineTittle = 1

def criar_interface(file_path=None):
    root = Tk()
    root.withdraw()
    if file_path is None:
        file_path = filedialog.askopenfilename(
            title="Selecione um arquivo Excel",
            filetypes=[("Arquivos Excel", "*.xlsx *.xls")]
        )
        if not file_path:
            print('Nenhum arquivo selecionado.')
            root.destroy()
            return None

    try:
        df = pd.read_excel(file_path, header=lineTittle)

        if df.empty:
            messagebox.showerror("Erro", "O arquivo selecionado está vazio.")
            root.destroy()
            return None

        # Obter informações do arquivo
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        novo_nome = f"{name}-resumo{ext}"

        # Criar janela Tkinter
        interface_root = Tk()
        interface_root.title("Configurações do Arquivo")
        interface_root.configure(bg='#050505')

        # Criar frame para organização
        frame = Frame(interface_root, bg='#050505')
        frame.pack(padx=20, pady=20)

        # Labels e Inputs
        Label(frame, text="Nome do Arquivo:", bg='#050505', fg='#fafafa').grid(row=0, column=0, sticky='w')
        Label(frame, text=base_name, bg='#050505', fg='#fafafa').grid(row=0, column=1, sticky='w')

        Label(frame, text="Nome do Arquivo Final:", bg='#050505', fg='#fafafa').grid(row=1, column=0, sticky='w')
        Label(frame, text=novo_nome, bg='#050505', fg='#fafafa').grid(row=1, column=1, sticky='w')

        Label(frame, text="Definir Linha de Títulos:", bg='#050505', fg='#fafafa').grid(row=2, column=0, sticky='w')
        entry_line_tittle = Entry(frame, bg='#fafafa')
        entry_line_tittle.insert(0, str(lineTittle))
        entry_line_tittle.grid(row=2, column=1)

        # Função para remover uma coluna da lista
        def remover_coluna(coluna):
            colunas_desejadas.remove(coluna)
            interface_root.destroy()  # Fechar a janela atual
            criar_interface(file_path)  # Recriar a interface com a lista atualizada

        # Adicionar retângulos para cada coluna desejada com botão de remoção
        num_colunas = 2
        for i, coluna in enumerate(colunas_desejadas):
            row = i // num_colunas + 3
            col = i % num_colunas

            frame_coluna = Frame(frame, bg='#1f1f1f', padx=5, pady=5, borderwidth=0, relief="flat")
            frame_coluna.grid(row=row, column=col, padx=10, pady=5, sticky='we')

            Label(frame_coluna, text=coluna, bg='#1f1f1f', fg='#fafafa', font=("Arial", 12)).pack(side='left')

            # Botão para remover coluna
            btn_remover = Button(frame_coluna, text="X", bg='#ff4d4d', fg='#fafafa', relief='flat',
                                command=lambda col=coluna: remover_coluna(col))
            btn_remover.pack(side='right')

        # Entry para adicionar novo título de coluna
        novo_titulo_entry = Entry(frame, bg='#fafafa')
        novo_titulo_entry.grid(row=row+1, column=0, columnspan=num_colunas, padx=10, pady=5, sticky='we')

        def adicionar_coluna():
            novo_titulo = novo_titulo_entry.get()
            if novo_titulo:
                colunas_desejadas.append(novo_titulo)
                interface_root.destroy()  # Fechar a janela atual
                criar_interface(file_path)  # Recriar a interface com a lista atualizada
            else:
                messagebox.showwarning("Aviso", "Por favor, digite um título para adicionar.")

        # Botão para adicionar novo título de coluna
        btn_adicionar = Button(frame, text="Adicionar", bg='#4CAF50', fg='#fafafa', relief='flat',
                              command=adicionar_coluna)
        btn_adicionar.grid(row=row+2, column=0, columnspan=num_colunas, padx=10, pady=5, sticky='we')

        def salvar_configuracoes():
            nonlocal file_path, dir_name, novo_nome
            global lineTittle
            lineTittle = int(entry_line_tittle.get())
            interface_root.destroy()  # Fechar a janela após salvar

            try:
                # Após fechar a interface, verificar se as colunas desejadas existem
                df = pd.read_excel(file_path, header=lineTittle)
                colunas_disponiveis = df.columns.tolist()
                colunas_para_filtrar = [coluna for coluna in colunas_desejadas if coluna in colunas_disponiveis]

                if not colunas_para_filtrar:
                    messagebox.showerror("Erro", "Nenhuma das colunas desejadas foi encontrada no arquivo.")
                else:
                    # Criar arquivo filtrado
                    df_filtrado = df[colunas_para_filtrar]
                    novo_caminho = os.path.join(dir_name, novo_nome)
                    df_filtrado.to_excel(novo_caminho, index=False)
                    messagebox.showinfo("Sucesso", f'Arquivo salvo como {novo_caminho}')
            except Exception as e:
                messagebox.showerror("Erro", f'Erro ao processar o arquivo: {e}')

            root.quit()  # Sair do loop mainloop após salvar

        # Botão para salvar
        Button(frame, text="Salvar", command=salvar_configuracoes).grid(row=row+3, column=0, columnspan=num_colunas, pady=10, sticky='we')

        interface_root.mainloop()

    except Exception as e:
        messagebox.showerror("Erro", f'Erro ao processar o arquivo: {e}')

    root.destroy()  # Certificar-se de fechar a janela de seleção de arquivo se ainda estiver aberta
