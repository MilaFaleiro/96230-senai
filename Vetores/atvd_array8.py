import os
os.system ("clear")
# Função que verifica se o número é positivo ou negativo com vetores

lista = []
numeros_positivos = 0
numeros_negativos = 0
soma_positivos = 0

for i in range(5):
    valor = int(input("Digite um número: "))
    lista.append(valor)
    
    if valor > 0:
        numeros_positivos += 1
        soma_positivos += valor
    else:
        numeros_negativos += 1
        
print(f"Lista de números positivos: {numeros_positivos}")
print(f"Lista de números negativos: {numeros_negativos}")
print(f"Lista de números digitados: {lista}")
print(f"Soma dos números negativos {soma_positivos}")
