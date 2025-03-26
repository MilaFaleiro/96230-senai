import os
os. system("clear")

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número: "))
    
    if numero < 0:
        break
    
    soma += numero
    quantidade += 1

if quantidade > 0:
        media = soma / quantidade
        print (f"A media dos números que você informou é: {media:.2}")
else:
        print("Você informou um número negativo, tente novamente")