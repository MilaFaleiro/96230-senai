import os
os. system("cls")
print("Somando os números.")
soma = 0
for i in range (4):
    nota = float(input(f"Digite a {i+1} nota: "))
    soma = soma + nota
    media = soma / 4
print(f"Média: {media}")
print("\nFim")