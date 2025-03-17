import os
os. system("cls")

print("Somando os números.")

soma = 0
for i in range (3):

    nota = float(input(f"Digite a {i+1} nota: "))

    soma = soma + nota
    media = soma / 3

if media > 7:
    print ("Aluno aprovado")
else: 
     print ("Aluno Reprovado")
print(f"Média: {media}")
print("\nFim")