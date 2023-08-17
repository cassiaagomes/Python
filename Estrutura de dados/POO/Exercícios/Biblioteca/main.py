from siscadastro import Autor, Livro, biblioteca

livros = []
autores = []

sistema = biblioteca(livros, autores)

autor_cassia = sistema.cadastrar_autor("Cassia", "Brasileira")
livro_novo = sistema.cadastrar_livro("Eu", 2023, autor_cassia)

sistema.exibir_livros()
