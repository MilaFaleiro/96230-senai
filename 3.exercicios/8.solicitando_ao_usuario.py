import os
os.system("clear")

numero_um = int(input("Digite um número: "))
operador = input("Digite a operação que deseja (+ - * /): ")
numero_dois = int(input("Digite um número: "))

match operador:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        resultado = "Opção inválida. "
print(f"\nSeu primeiro número foi: {numero_um}")
print(f"Seu operador: {operador}")
print(f"Seu segundo número foi: {numero_dois}")
print(f"O resultado é: {resultado}")
        
    