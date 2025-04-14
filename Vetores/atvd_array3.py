import os
os.system("clear")

lista_notas =[]

for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma / len(lista_notas)

if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"
print(f"A soma das notas é: {soma}")
print(f"A média das notas é: {media:.2f}")
print(f"Resultado: {resultado}")