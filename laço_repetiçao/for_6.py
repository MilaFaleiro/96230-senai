import os
os. system("cls")

print("somando os números")
soma = 0
for i in range (5):
    nota = float(input(f"Digite a {i+1} nota: "))
    soma = soma + nota
print(f"Soma: {soma}")
print("\nFim")