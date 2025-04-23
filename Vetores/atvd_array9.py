import os
os.system("clear")

lista = []

for i in range(5):
    valor =int(input("Digite um número: "))
    if valor < 0:
        lista.append (0) 
        lista.remove (valor)

    else:
        valor = lista
print(f"Valor" {lista}) 