import os
os.system("clear")

quantidade_numeros = 6
lista_numeros = []
pares = 0
impares = 0

for i in range (quantidade_numeros):
    numero= int(input("Digite um número: "))
    lista_numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
for i, numero in enumerate(lista_numeros, start=1):
    print (f"{i}º: {numero}")

print(f"\nNúmeros Pares: {pares}")
print(f"\nNúmeros Impares: {impares}")
