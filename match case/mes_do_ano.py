import os
os.system("clear")

dia = input("Digite um número que represente um dia da semana: ")

match dia:
    case"1":
        print("\nJaneiro")

    case "2":
        print("\nFevereiro")

    case "3":
        print("\nMarço")

    case "4":
        print("\nAbril")

    case "5":
        print("\nMaio")

    case "6":
        print("\nJunho")

    case "7":
        print("\nJulho")

    case "8":
        print("\nAgosto")

    case "9":
        print("\nSetembro")

    case "10":
        print("\nOutubro")

    case "11":
        print("\nNovembro")

    case "12":
        print("\nDezembro")

    case _:
        print("\nDia inválido.")


print("===FIM===")
