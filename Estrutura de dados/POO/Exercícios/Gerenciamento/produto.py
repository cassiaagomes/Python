class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    
    def exibir_info(self):
        print(f'Produto: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.qtd}')
        