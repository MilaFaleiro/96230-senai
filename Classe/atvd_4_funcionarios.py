import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Pessoa:
    #Atributos: são variaveis que pertence a classe
    nome: str
    data_nascimento: int
    rg: int
    cpf: int

#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    
    def exibir_dados (self):
        print (f"Nome: {self.nome} \nData de nascimento: {self.data_nascimento}\nRegistro geral: {self.rg}\nCpf: {self.cpf}\n ")
lista_pessoas= []
QUANTIDADE_PESSOAS = 5

#Atribuindo dados ao paciente1.
for i in range (QUANTIDADE_PESSOAS):
    pessoa = Pessoa(
                        nome= input("Digite seu nome : "),
                        data_nascimento = int(input("Digite sua data de nascimento: " )),
                        rg = int(input("Digite seu rg: ")),
                        cpf = int(input("Digite o cpf: "))
                    )
    lista_pessoas.append(pessoa)

#Salvando em um arquivo .txt
nome_arquivo = "Funcionarios.txt"
with open (nome_arquivo, "w") as arquivo_pessoa: # "w" apaga os anteriores, "a" acumula, vai juntando com os antigos.
    for pessoa in lista_pessoas:
        arquivo_pessoa.write(f"{pessoa.nome}\n{pessoa.data_nascimento}\n{pessoa.rg}\n{pessoa.cpf}\n")

print ("Dados salvos com sucesso.")

#Exibindo dados da pessoa.
print("\nExibindo dados.")
for pessoa in lista_pessoas:
    pessoa.exibir_dados()