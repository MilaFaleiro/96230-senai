import os
os.system("clear")

valor = 0
total = 0
lista_pratos = []

while True:
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
                print("Você escolheu Picanha")
                valor = 25.00
                prato = "Picanha"
            case 2:
                print("Você escolheu Lasanha")
                valor = 20.00
                prato = "Lasanha"
            case 3:
                print("Você escolheu Strogonoff")
                valor = 18.00
                prato = "Strogonoff"
            case 4:
                print("Você escolheu Bife acebolado")
                valor = 15.00
                prato = "Bife acebolado"
            case 5:
                print("Você escolheu Pão com ovo")
                valor = 05.00
                prato = "Pão com ovo"
            case _:
                print ("\nDesculpe, não existe essa opção. Digite novamente: ")

    lista_pratos.append(prato)
    total += valor

    continuar = input("\nDeseja adicionar mais um pedido? (s/n): ").strip().lower()

    if continuar == "s":
                continue
    elif continuar != "n":
            print(f"\nTotal do pedido: {total:.2f}")
            print("Opção inválida, digite 's' ou 'n' ")
            break
    
    print(f"\nTotal á pagar: R$ {total:.2f}")
    for prato in lista_pratos:
            print(f"Seu prato escolhido foi: {prato}")

    print("\nPedido finalizado com sucesso. Muito obrigado!! Volte sempre.")
    break