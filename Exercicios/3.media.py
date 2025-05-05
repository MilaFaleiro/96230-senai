import os
os.system("clear")

primeira_nota= float(input("Olá digite sua primeira nota: "))
segunda_nota= float(input("Olá digite sua primeira nota: "))
terceira_nota= float(input("Olá digite sua primeira nota: "))


soma= primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print(f"Sua média é: {media}")

if media < 7: 
    print ("Aluno Reprovado!")
else: 
    print ("Aluno aprovado!")





