# Elabore um algoritmo usando operações lógicas para solicitar ao usuário 2 números e escrever:
# Os 2 números informados.
# O maior número
# O menor número
import os
os.system("clear")

valor_um = float(input("Olá, digite um numero:" ))
valor_dois = float(input("Digite outro numero:" ))

if valor_um < valor_dois:
    menor = valor_um
    maior = valor_dois
else: 
    menor= valor_dois
    maior= valor_um

print(f"O primeiro número que você digitou foi: {valor_um}")
print(f"O segundo número que você digitou foi: {valor_dois}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
