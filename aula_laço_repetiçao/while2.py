import os
os.system("cls")

soma = 0

while True:
    print("""

Código \t Prato \t Valor

1 \t Picanha \t R$ 25,00
2 \t Lasanha \t R$ 20,00
3 \t Strogonoff \t R$ 18,00
4 \t Bife acebolado\t R$ 15,00
5 \t Pão com ovo \t R$ 5,00                                                                                             
""")
    opcao = int(input("Olá digite o código da sua preferência: "))
    match opcao: 
        case 1:
            print("Seu prato foi picanha.")
            valor = 25
        case 2:
            print("Seu prato lasanha.")
            valor = 20
        case 3:
            print("Seu prato foi strogonoff.")
            valor = 18
        case 4:
            print("Seu prato foi bife acebolado.")
            valor = 15
        case 5:
            print("Seu prato foi pão com ovo.")
            valor = 5
        case _:
            print("Opção inválida")
            
    soma += valor
    
    continuar = input("Deseja pedir outro prato? Digite 1 para Sim e 2 para não ")
    
    if continuar == "1":
        
        break