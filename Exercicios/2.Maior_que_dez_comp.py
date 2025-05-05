import os
os.system("clear")

#Elabore um algoritmo par solicicitar ao usuário um valor e escrever a mensagem: 
# É MAIOR QUE 10! Se o valor lido for maior que 10.
#  caso contrário escrever: NÃO É MAIOR QUE 10!
# Verifique se o número digitado é igaul a 10, caso seja, escreva "O número é igual a 10!"

idade = int(input("Olá usuário, digite um número: "))

if idade > 10:
    print ("Parabéns!!!! é maior que 10")

elif idade < 10:
     print ("Não é maior que 10")

else: 
    print ("O número é igual a 10!")