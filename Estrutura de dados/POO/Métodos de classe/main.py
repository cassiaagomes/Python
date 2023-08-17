class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    @property
    def nome(self):
        return self._novo_nome

    @nome.setter
    def nome(self, valor):
        self._novo_nome = valor.title()


    #get
    @property
    def preco(self):
        return self._novo_preco
    
    #set
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        
        self._novo_preco = valor


p1 = Produto('CAMISETA', 10)
p1.desconto(50)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15')
p2.desconto(10)
print(p2.nome, p2.preco)
