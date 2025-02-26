import os
os.system("clear")

opcao = int(input("""
Código \t Prato \t Valor
1 \t Picanha \t R$ 25,00
2 \t Lasanha \t R$ 20,00
3 \t Strogonoff \t R$ 18,00
4 \t Bife acebolado\t R$ 15,00
5 \t Pão com ovo \t R$ 5,00                  
Digite a opção desejada:                                                                                      
"""))
match opcao:
    case 1:
        print("Seu pedido foi picanha e o valor é R$ 25,00")
    case 2:
        print("Seu pedido foi Lasanha e o valor é R$ 20,00")
    case 3:
        print("Seu pedido foi Strogonoff e o valor é R$ 18,00")
    case 4:
        print("Seu pedido foi Bife acebolado e o valor é R$ 15,00")
    case 5:
        print("Seu pedido foi Pão com ovo e o valor é R$ 5,00")
    case _:
        print("Opção inválida.")
        
print("===FIM===")
   
    

