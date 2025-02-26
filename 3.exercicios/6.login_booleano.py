import os
os.system("clear")

email_cadastrado = "marta"
senha_cadastrado = "0812"

email = input("Olá, digite seu email:" )
senha = input("Digite sua senha:" )

if email == email_cadastrado and senha == senha_cadastrado:
    print ("Bem vindo")
else:
    print ("Login ou senha inválidos")

