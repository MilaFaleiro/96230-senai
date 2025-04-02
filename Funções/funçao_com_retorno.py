import os
os.system ("clear")

#Função com retorno
def calcular_media (Primeira_nota, segunda_nota):
    soma = Primeira_nota + segunda_nota
    media = soma / 2
    return media

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

media = calcular_media (primeiro_numero, segundo_numero)

print(f"Média: {media}")