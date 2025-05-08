# Cria a interfase gráfica

#  Importa as bibliotecas necessárias
import tkinter as tk
from tkinter import filedialog, messagebox
from planilha import ler_credenciais
from login import testar_credenciais

def iniciar_interface():

    def selecionar_arquivo(): # Função para selecionar o arquivo

        # pega o caminho do arquivo
        caminho = filedialog.askopenfilename(
            title="Selecione uma planilha de credenciais",
            filetypes=[("Arquivos Excel", "*.xlsx")],
        )
        
        if caminho: # verifica se o caminho foi selecionado
            try: # se o caminho foi selecionado, tenta ler as credenciais
                credenciais = ler_credenciais(caminho)
                testar_credenciais(credenciais)
                messagebox.showinfo("Concluido", "Teste concluido com sucesso")
            except Exception as e: # caso ocorra algum erro informa o mesmo
                messagebox.showerror("error", f"Ocorreu um erro: \n{e}")

    # define o titulo da janela
    root = tk.Tk()
    root.title("Validador de Logins do Valorant")

    # define a largura e altura da janela
    largura, altura = 300, 150
    root.geometry(f"{largura}x{altura}")
    root.resizable(False, False)

    btn = tk.Button(root, text="Selecionar Planilha", command=selecionar_arquivo, width=20, height=2)
    btn.pack(pady=40)

    root.mainloop()