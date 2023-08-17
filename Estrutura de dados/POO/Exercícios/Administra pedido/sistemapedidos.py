from pedido import *
from produto import *

class SistemaPedidos:
    def __init__(self):
        self.pedidos = [] 
    
    def adicionar_pedidos(self, pedido):
        self.pedidos.append(pedido)
    
    def exibir_pedidos(self):
        for pedido in self.pedidos:
            print(f"Cliente: {pedido.cliente}")
            print("Itens:")
            for item in pedido.itens:
                print(f" - {item.nome}: {item.quantidade} unidades")
            print(f"Total: R$ {pedido.total:.2f}")
    
    def cadastrar_produto(self, nome, preco, quantidade):
        produto = Produto(nome, preco, quantidade)
        return produto
    
    def calcular_valor_total(self, pedido):
        total = 0
        for item in pedido.itens:
            total += item.preco * item.quantidade
        return total

    
