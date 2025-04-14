import os
os.system("clear") 

lista = []
quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_impares = 0

for i in range(6):
    numero = int(input(f"Digite o {i+1}º número: "))
    lista.append(numero)

    if numero % 2 == 0:
            quantidade_pares += 1
            soma_pares += numero
    else:
            quantidade_impares += 1
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")