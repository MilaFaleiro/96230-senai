import os
os.system("clear")

dia = input("Digite um número que represente um dia da semana: ")

match dia:
    case"1":
        print("\nHoje é segunda feira dia útil")

    case "2":
        print("\nHoje é terça feira dia útil")

    case "3":
        print("\nHoje é quarta feira dia útil")

    case "4":
        print("\nHoje é quinta feira dia útil")

    case "5":
        print("\nHoje é sexta feira dia útil")

    case "6" | "7":
        print("\nHoje é fim de semana!")

    case _:
        print("\nDia inválido.")


print("===FIM===")
