import os
os.system("clear")

valor_um = float(input("Olá, digite um numero:" ))
valor_dois = float(input("Digite outro numero:" ))

soma= valor_um + valor_dois

media= soma/2

produto= valor_um * valor_dois

if valor_um < valor_dois:
    menor = valor_um
    maior = valor_dois
else: 
    menor= valor_dois
    maior= valor_um

print(f"A media de ambos os números são: {media}")
print(f"O produto é: {produto}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")
