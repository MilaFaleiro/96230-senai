import os
from dataclasses import dataclass
os.system ("clear")

@dataclass
class Autor:
    nome: str
    biografria: str
@dataclass
class Livro:
    titulo: str
    ano: int
    autor = Autor

    def exibir_detalhes (self):
        print(f"Nome: {self.nome} \nTitulo: {self.titulo} \nAno: {self.ano}")
print(f"---Solicitando dados---")
livro = Livro (
            titulo = input("Digite o título do livro: "),
            ano =int(input("Digite o ano de publicação: ")),
            autor = Autor(
                nome = input("Digite o nome do autor: "),
                biografria = input("Digite a biografia do autor: ")
            )
)

print("\n --Salvando Dados--")
#Salvando em um arquivo .txt
nome_arquivo = "Livro.txt"
with open (nome_arquivo, "a") as arquivo_livros:
    arquivo_livros.write(f"Titulo: {livro.titulo}\nAno: {livro.ano}\nAutor: {livro.autor}")