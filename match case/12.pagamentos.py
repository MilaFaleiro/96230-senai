#Solicite que o usuário informe o valor de um produto e a forma de pagamento.
#1 - Pagamento à vista; 2 - Pagamento à prazo.
#Se o produto for pago à vista aplique um desconto de 10% antes de mostrar o valor final, senão informe o mesmo valor do produto. Se for escolhida a opção de pagamento à prazo, solicite que o usuário digite a quantidade de parcelas que ele deseja pagar. Podendo parcelar em até 6 vezes. 
#No final, mostre: Se o pagamento for à vista: 
                    #Valor do produto: R$ 100,00
                    #Forma de pagamento: à vista
                    #Valor do desconto: R$ 10,00
                    #Total a pagar: R$ 90,00

#Se o pagamento for à prazo: 
#Valor do produto: R$ 100,00
#Forma de pagamento: à prazo
#Quantidade de parcelas: 6
#Valor por parcela: R$ 16,66
#Total à prazo: R$ 100,00

import os
os.system("cls")

valor = float(input("Digite o valor do produto: "))

print("\nOlá usuário, escolha a forma de pagamento: ")
print("\n1- Pagamento á vista")
print("2- Pagamento à prazo")

pagamento = int(input("\nDigite a opção desejada (1 ou 2): "))

match pagamento:

    case 1: 
        desconto = valor * 0.1
        total = valor - desconto
        
        print("\nResumo da compra: ")
        print(f"Valor do produto: R$ {valor:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    case 2:
        parcelas = int(input("\nDigite a quantidade de parcelas (No máximo 6): "))

        if 1 <= parcelas <= 6:
            parcelamento = valor / parcelas
    
            print("\nResumo da compra: ")
            print(f"Valor do produto: R$ {valor:.2f}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: {parcelamento:.2f}")
            print(f"Total a pagar: {valor:.2f}")
        
        else:
            print("Número de parcelas inválido. Escolha entre 1 e 6.")

    case _:
            print("Opção inválida. Escolha entre 1 e 2.")

print("\nObrigado! e volte sempre 😘💕")