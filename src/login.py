# src/login.py

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from planilha import salvar_resultados

def testar_credenciais(credenciais_df):
    sucesso = []
    erro = []

    for _, linha in credenciais_df.iterrows():
        usuario = linha['usuario']
        senha = linha['senha']

        if testar_login(usuario, senha):
            sucesso.append(linha)
        else:
            erro.append(linha)

    if sucesso:
        salvar_resultados(pd.DataFrame(sucesso), sucesso=True)
    if erro:
        salvar_resultados(pd.DataFrame(erro), sucesso=False)

def testar_login(usuario, senha):
    try:
        options = Options()
        options.add_argument("--incognito")
        # options.add_argument("--headless")  # Se quiser rodar em segundo plano, remova o comentário
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://playvalorant.com/pt-br/platform-selection/")

        # Clica no botão PC
        driver.find_element(By.XPATH, '(//a[@data-testid="cta-primary"])[1]').click()

        # Clica no último botão "Fazer login"
        botoes = driver.find_elements(By.XPATH, '//a[@data-testid="cta-primary"]')
        botoes[-1].click()

        # Preenche login
        driver.find_element(By.NAME, "username").send_keys(usuario)
        time.sleep(0.3)
        driver.find_element(By.NAME, "password").send_keys(senha)
        driver.find_element(By.XPATH, '//button[@data-testid="btn-signin-submit"]').click()

        # Aguardar até que o usuário resolva o CAPTCHA manualmente
        print("Por favor, resolva o CAPTCHA manualmente e pressione Enter para continuar...")
        input("Pressione Enter quando terminar de resolver o CAPTCHA...")

        time.sleep(1)

        # Verifica se login teve sucesso
        sucesso = "download" in driver.current_url
        driver.quit()
        return sucesso

    except Exception as e:
        print(f"Erro ao testar {usuario}: {e}")
        return False