from anticaptchaofficial. import AnticaptchaRecaptchaV2Proxyless


try:
    from anticaptchaofficial.recaptchaV2proxyless import AnticaptchaRecaptchaV2Proxyless
    print("Importação bem-sucedida!")
except ImportError as e:
    print(f"Erro na importação: {e}")