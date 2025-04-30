import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Paciente:
    #Atributos: são variaveis que pertence a classe
    nome: str
    idade: int

#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    
    def exibir_dados (self):
        print (f"Nome: {self.nome} \nIdade: {self.idade}\n")
lista_pacientes = []
QUANTIDADE_PACIENTES = 2

#Atribuindo dados ao paciente1.
for i in range (QUANTIDADE_PACIENTES):
    paciente = Paciente(
                        nome= input ("Digite seu nome: "),
                        idade= int(input("Digite sua idade: " ))
                    )
    lista_pacientes.append(paciente)

#Salvando em um arquivo .txt
nome_arquivo = "Dados_paciente.txt"
with open (nome_arquivo, "w") as arquivo_pacientes: # "w" apaga os anteriores, "a" acumula, vai juntando com os antigos.
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")

print ("Dados salvos com sucesso.")

#Exibindo dados do paciente.
print("\nExibindo dados.")
for paciente in lista_pacientes:
    paciente.exibir_dados()