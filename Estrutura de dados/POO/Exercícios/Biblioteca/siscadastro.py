class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome #atribuir none quando os valores começarem vazios
        self.nacionalidade = nacionalidade
    
    def exibir_info(self):
        print(f'Autor: {self.nome}')
        print(f'Nacionalidade: {self.nacionalidade}')

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
    
    def exibir_info(self):
        print(f'Livro: {self.titulo}')
        print(f'Ano: {self.ano}')
        print(f'Autor: {self.autor}')

class biblioteca:
    def __init__(self, livros, autores):
        self.livros = livros
        self.autores = autores

    def cadastrar_autor(self, nome, nacionalidade):
        autor = Autor(nome, nacionalidade)
        self.autores.append(autor)
        return autor

    def cadastrar_livro(self, titulo, ano, autor):
        livro = Livro(titulo, ano, autor)
        self.livros.append(livro)
        return livro

    def exibir_autores(self):
        print("Autores:")
        for autor in self.autores:
            autor.exibir_info()

    def exibir_livros(self):
        print("Livros:")
        for livro in self.livros:
            livro.exibir_info()

