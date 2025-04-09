import os
os.system ("clear")

soma= 0
def calcular (soma):
    return soma / 2
for i in range (2):

    nota=float(input("Digite a primeira nota: "))
    soma += nota
    media = calcular (soma)
print (f"Média {media}")