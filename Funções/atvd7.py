import os
os.system ("clear")

def calcular_media (Primeira_nota, segunda_nota):
    soma = 0
    soma = Primeira_nota + segunda_nota
    media = soma / 2
    return media

def verificar_resultado(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
    

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

media = calcular_media (primeiro_numero, segundo_numero)

print(f"Média: {media}")