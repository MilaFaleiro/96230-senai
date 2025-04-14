import os
os.system("clear")

numero =[]

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    numero.append(num)
    maximo = max(numero)
    minimo = min(numero)
print(f"O maior número é: {maximo}")
print(f"O menor número é: {minimo}")

    

