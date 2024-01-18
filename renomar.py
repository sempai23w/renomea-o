import os
import tkinter as tk
from tkinter import filedialog

def renomear_arquivos(diretorio, sigla_antiga, sigla_nova):
    lista_arquivos = os.listdir(diretorio)

    for nome_arquivo in lista_arquivos:
        if nome_arquivo.startswith(sigla_antiga):
            novo_nome = nome_arquivo.replace(sigla_antiga, sigla_nova)
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            caminho_novo = os.path.join(diretorio, novo_nome)
            os.rename(caminho_antigo, caminho_novo)
            print(f"Arquivo renomeado: {nome_arquivo} -> {novo_nome}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    diretorio_entry.delete(0, tk.END)
    diretorio_entry.insert(0, diretorio)

def renomear():
    diretorio = diretorio_entry.get()
    sigla_antiga = sigla_antiga_entry.get()
    sigla_nova = sigla_nova_entry.get()
    
    renomear_arquivos(diretorio, sigla_antiga, sigla_nova)
    resultado_label.config(text="Renomeação concluída!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Renomeador de Arquivos")
janela.configure(bg='#1E1E1E')  # Cor de fundo escura

# Criar e posicionar os widgets na janela
tk.Label(janela, text="Diretório:", bg='#1E1E1E', fg='white', font=('Arial', 10)).grid(row=0, column=0, sticky="E", padx=5, pady=5)
diretorio_entry = tk.Entry(janela, width=50, bg='#303030', fg='white', font=('Arial', 10))
diretorio_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(janela, text="Selecionar", command=selecionar_diretorio, bg='#303030', fg='white', font=('Arial', 10)).grid(row=0, column=2, padx=5, pady=5)

tk.Label(janela, text="Sigla Antiga:", bg='#1E1E1E', fg='white', font=('Arial', 10)).grid(row=1, column=0, sticky="E", padx=5, pady=5)
sigla_antiga_entry = tk.Entry(janela, width=30, bg='#303030', fg='white', font=('Arial', 10))
sigla_antiga_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(janela, text="Sigla Nova:", bg='#1E1E1E', fg='white', font=('Arial', 10)).grid(row=2, column=0, sticky="E", padx=5, pady=5)
sigla_nova_entry = tk.Entry(janela, width=30, bg='#303030', fg='white', font=('Arial', 10))
sigla_nova_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(janela, text="Renomear", command=renomear, bg='#303030', fg='white', font=('Arial', 10)).grid(row=3, column=1, pady=10)

resultado_label = tk.Label(janela, text="", bg='#1E1E1E', fg='white', font=('Arial', 10))
resultado_label.grid(row=4, column=0, columnspan=3)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
