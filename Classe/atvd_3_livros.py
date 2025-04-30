import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Livro:
    #Atributos: são variaveis que pertence a classe
    nome: str
    autor: str
    categoria: str
    preço: float

#Método: é uma função que pertence a classe.
#Este método para exibir dados do paciente.
    
    def exibir_dados (self):
        print (f"Nome: {self.nome} \nAutor: {self.autor}\nCategoria: {self.categoria}\nPreço: {self.preço}\n ")
lista_livros = []
QUANTIDADE_LIVROS = 3

#Atribuindo dados ao paciente1.
for i in range (QUANTIDADE_LIVROS):
    livro = Livro(
                        nome= input("Digite o nome do livro: "),
                        autor= input("Digite o autor: " ),
                        categoria = input("Digite a categoria do livro: "),
                        preço = float(input("Digite o valor do livro: "))
                    )
    lista_livros.append(livro)

#Salvando em um arquivo .txt
nome_arquivo = "Dados_livros.txt"
with open (nome_arquivo, "w") as arquivo_livros: # "w" apaga os anteriores, "a" acumula, vai juntando com os antigos.
    for livro in lista_livros:
        arquivo_livros.write(f"{livro.nome}\n {livro.autor}\n {livro.categoria}\n {livro.preço}\n")

print ("Dados salvos com sucesso.")

#Exibindo dados do livro.
print("\nExibindo dados.")
for livro in lista_livros:
    livro.exibir_dados()