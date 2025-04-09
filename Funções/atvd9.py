import os
os.system("clear")

def inflacionar(valor):
    if valor < 100:
        resultado = valor * 1.10
    else:
        resultado = valor * 1.20   
        return resultado

def desconto (valor):
    if preço_produto < 100:
        resultado = valor * 0.10
    else:
        resultado = valor * 0.20   
        return resultado
    
preço_produto = float(input("Digite o preço do produto: "))

preço_taxa = inflacionar(preço_produto)
preço_desconto = desconto(preço_produto)

print(f"O preço do produto com a taxa de inflação é: R$ {preço_taxa:.2f}")
print(f"O preço do produto com desconto é: R$ {preço_desconto:.2f}")
