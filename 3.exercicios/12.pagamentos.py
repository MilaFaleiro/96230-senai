import os
os.system("clear")

valor = float(input("Digite o valor do produto: "))
pagamento = int(input("Digite a forma de pagamento: "))

match pagamento:
    case 1: 
        desconto = valor * 0.1
