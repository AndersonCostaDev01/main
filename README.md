# ✅ Validador de Logins do Valorant

## 📌 Objetivo

Este projeto automatiza o processo de verificação de credenciais do **Valorant (Riot Games)**. Ele utiliza automação com **Selenium** para simular logins e registra os resultados em **planilhas Excel (.xlsx)** para posterior análise.

---

## 🚀 Como funciona

O script:

1. Acessa o site oficial do Valorant.
2. Navega até a página de login.
3. Utiliza dados de uma planilha com **usuários e senhas**.
4. Preenche os campos do formulário e tenta fazer o login.
5. Registra os **logins bem-sucedidos** em uma planilha chamada `logins_sucesso.xlsx`.
6. Registra os **logins com falha** em outra planilha chamada `logins_erro.xlsx`.

---

## ✅ Pré-requisitos

Antes de executar o projeto, você precisa ter:

- Python 3.8 ou superior
- Google Chrome
- ChromeDriver compatível com sua versão do navegador
- Bibliotecas Python:
  - `selenium`
  - `openpyxl`
  - `tkinter`
  - `pandas`
- Para gerar o executável `.exe`:
  - `pyinstaller`

Instale as bibliotecas com:

```bash
pip install selenium openpyxl pandas
```

---

## 🛠️ Como iniciar

### 1. Acesse a página inicial do Valorant:

```
https://playvalorant.com/pt-br/platform-selection/
```

### 2. Clique no botão "PC":

```html
<a
  role="button"
  href="https://playvalorant.com/pt-br/download/"
  data-testid="cta-primary"
  >PC</a
>
```

### 3. Clique no botão "Fazer login":

> ⚠️ Existem 4 elementos iguais. Clique no **último**.

```html
<a role="button" href="javascript: void(0)" data-testid="cta-primary"
  >Fazer login</a
>
```

### 4. Na página de login:

- Preencha os inputs `username` e `password`
- Clique no botão `data-testid="btn-signin-submit"`

---

## 📄 Como saber se o login foi bem-sucedido?

- Sucesso ➜ redirecionamento para `https://playvalorant.com/pt-br/download/`
  ➜ Salvo em `logins_sucesso.xlsx`
- Erro ➜ Não redireciona ou retorna erro
  ➜ Salvo em `logins_erro.xlsx`

---

## 📂 Estrutura da planilha de entrada

Arquivo Excel `usuarios_senhas.xlsx`:

| usuario | senha    |
| ------- | -------- |
| teste2  | dasf2asd |
| teste1  | asdf1234 |

---

## 📦 Gerar o executável

Após validar o funcionamento com `main.py`, gere o `.exe` com:

```bash
pyinstaller --onefile --noconsole main.py
```

> Use `--noconsole` se desejar esconder o terminal ao abrir o programa.

---

## 💡 Extras

- Interface gráfica em Tkinter (opcional)
- Reabertura automática em sessão anônima por login
- Logs de tentativa por usuário
