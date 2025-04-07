import os
os.system ("clear")
def verificar_numero(valor):
    
    if valor > 0:
        print("É positivo")

    else:
        print ("É negativo.")

numero = int(input("Digite um número: "))
verificar_numero (numero)
print("Acabouse")

