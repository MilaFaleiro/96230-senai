import os
os. system ("clear")

def calcular (idade):
    resultado = 2025 - idade
    return resultado

print("Calculando ano de nascimento")
ano_nascimento= int(input("Digite o ano de nascimento: "))

idade = calcular (ano_nascimento)

print("\n Resultado ")
print(f"Você nasceu no ano de {ano_nascimento}.")

