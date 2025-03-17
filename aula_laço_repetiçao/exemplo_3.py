import os
import time

os. system("cls")
contagem = int(input("Olá, digite um número:" ))

print("\nContagem regressiva")
for i in range (contagem,0,-1):
    print(f"Valor da variável i: {i}")
    time.sleep(1)
print("Fimm") 
