import os
os.system ("clear")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

def calcular_imc (peso, altura): 
    imc = peso / altura ** 2
    return imc
if calcular_imc < 18.5:
    print ("Abaixo do peso")
elif calcular_imc < 24.9:
    print ("Peso normal")
elif calcular_imc < 29.9:
    print ("Sobrepeso")
if calcular_imc < 34.9:
    print ("Obesidade grau 1")
if calcular_imc < 39.9:
    print ("obesidade grau 2")
else:
    print ("Obesidade grau 3")
print(f"Seu IMC é: {calcular_imc (peso, altura)}")