import os
os. system("clear")

def numero_par (numero):
    if numero % 2 == 0:
        print("Esse número é par.")
    else:
        print("Esse número é impar.") 
        
numero = int(input("Digite um número: "))
numero_par (numero)
print("Acabouse")
