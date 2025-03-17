import os
os. system("cls")


for i in range (5):
    nota = int(input("Digite um número: "))
    
    if nota % 2 == 0:
        print(f"{nota} é par")
    else:
        print(f"{nota} é ímpar")
        