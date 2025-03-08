import os
os.system("cls")

#Faça um programa que calcule o "peso ideal" de um usuário de acordo com um caractere identificador de sexo("M" para masculino  ou "F para feminino") inserido pelo mesmo. A fórmula para cada um dos dois casos está definida abaixo.
#Caso "M", utilize a fórmula: (72.7 x altura)-58
#Caso "F", utilize a fórmula: (62.1 x altura)-44.7
altura = float(input("Olá usuário, para saber seu peso ideal digite sua altura: "))

sexo = input("Digite seu sexo (M para masculino e F para feminino): ")

match sexo:

        case "M": 
            peso_ideal = (72.7 * altura) - 58
            print(f"Seu peso ideal é:{peso_ideal:.2f} kg")

        case "F":
            peso_ideal = (62.1 * altura) -44.7
            print(f"Seu peso ideal é:{peso_ideal:.2f} kg")
        
        case _: 
            print("Opção inválida")