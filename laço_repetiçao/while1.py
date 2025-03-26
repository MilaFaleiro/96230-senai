import os
os.system("cls")

QUANTIDADE_NOTAS =  3
soma = 0 

for i in range (QUANTIDADE_NOTAS):
    while True:
        nota = float(input("Digite sua nota: "))
        
        if nota < 0 or nota > 10:
            print ("A nota deve ser entre 0 e 10")
        else:
            soma += nota
            break
            
media = soma /QUANTIDADE_NOTAS
            
    
if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resultado = "Recuperação"
else :
    resultado = "Reprovado"

print(f"\nMédia {media}")
print(f"\nResultado {resultado}")
