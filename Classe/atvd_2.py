import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Paciente:
    #Atributos: são variaveis que pertence a classe
    nome: str
    idade: int
    peso: float
    altura:float

#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    
    def exibir_dados (self):
        print (f"Nome: {self.nome} \nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\n")
lista_pacientes = []
QUANTIDADE_PACIENTES = 4

#Atribuindo dados ao paciente1.
for i in range (QUANTIDADE_PACIENTES):
    paciente = Paciente(
                        nome= input ("Digite seu nome: "),
                        idade= int(input("Digite sua idade: " )),
                        peso= float(input("Digite seu peso: ")),
                        altura= float(input("Digite sua altura: "))
                    )
    lista_pacientes.append(paciente)

#Exibindo dados do paciente.
print("\nExibindo dados.")
for paciente in lista_pacientes:
    paciente.exibir_dados()