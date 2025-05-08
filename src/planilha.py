# arquivo que ira fazer a leitura da planilha 

# Importa as bibliotecas necessárias
import pandas as pd

def ler_credenciais(caminho_arquivo): # Função para ler as credenciais da planilha
    df = pd.read_excel(caminho_arquivo)
    
    # Verifica se as colunas 'usuario' e 'senha' estao na planilha
    if 'usuario' not in df.columns or 'senha' not in df.columns:
        raise Exception("A planilha deve conter as colunas 'usuario' e 'senha'")
    return df

def salvar_resultados(df, sucesso=True): # Função para salvar os resultados em uma planilha Excel
    nome_arquivo = "logins_sucesso.xlsx" if sucesso else "logins_erro.xlsx"
    df.to_excel(nome_arquivo, index=False)