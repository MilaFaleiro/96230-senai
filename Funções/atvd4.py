import os
os.system ("clear")

numero = int(input("Digite um número: "))

def tabuada ():
    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")
print ("--Tabuada--")
tabuada ()