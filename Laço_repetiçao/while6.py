import os
os. system("clear")

while True:
    opçao = int(input("""
CÓDIGO  | DESCRIÇÃO
    1   | Adicionar pessoa
    2   | Exibir Resultados
    3   | Sair
    
"""))
    match opçao:
        case 1:
            quantidade = int(input(f"Digite a quantidade de pessoas: "))
            for i in range (quantidade):
                
                idade = int(input("Digite sua idade: "))
                salario = int(input("Digite seu salário: "))
                sexo = input("Qual o seu gênero? \nDigite 'f' ou 'm': ").upper ()
                
                media_salario += salario
                
                if idade > maior_idade:
                    maior_idade = idade

                if idade < menor_idade:
                    menor_idade = idade

                if sexo == "F" and salario >= 5000:
                    mulheres_salario += 1
                    os.system ("cls")
        case 2: 
            if quantidade > 0:
                media_salario = media_salario / quantidade

                print (f"Media de salário do grupo: {media_salario:.2f}")
                print (f"Maior idade do grupo: {maior_idade}")
                print (f"Menor idade do grupo: {menor_idade}")
                print (f"Quantidade de mulheres com salário acima de 5000: {mulheres_salario}")
            else:
                print("Nenhuma pessoa cadastrada.")
        case 3:
            exit ("Programa finalizado")
        case _: 
            print ("Opção inválida!")
    