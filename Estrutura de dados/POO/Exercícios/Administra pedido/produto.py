class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def exibir_info(self):
        print(f'Produto: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.quantidade}')

#produto = Produto("Camiseta", 29.99, 50)
#produto.exibir_info()