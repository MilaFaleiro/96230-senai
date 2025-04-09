import os
os.system("clear")

def conversor_metros (valor):
    return metros * 100;
print("Convertendo cm para metros")
metros = float(input("Digite um número: "))

centimetros = conversor_metros(metros)

print("\n Resultado ")
print(f"{metros} metros é igual a {centimetros} centímetros.")
