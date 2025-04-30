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

#Atribuindo dados ao paciente1.
paciente1 = Paciente(
                        nome= input ("Digite seu nome: "),
                        idade= int(input("Digite sua idade: "))
                    )

#Exibindo dados do paciente.
print("\nExibindo dados.")
paciente1.exibir_dados()