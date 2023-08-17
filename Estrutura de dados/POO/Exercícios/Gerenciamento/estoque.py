from produto import *

class Estoque:
    def __init__(self):
        self.produtos = []
        self.quantidade = None
    
    def cadastrar_produto(self, nome, preco, quantidade):
        produto = Produto(nome, preco, quantidade)
        self.produtos.append(produto)
        return produto

    def atualizar_quantidade(self, nome_produto, nova_quantidade):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                produto.qtd = nova_quantidade
                break
        else:
            print(f'Produto "{nome_produto}" não encontrado.')

    def procurar_produto(self):
        nomeproduto = input("Informe o nome do produto: ")
        for produto in self.produtos:
            if nomeproduto == produto.nome:
                print(f"Produto: {nomeproduto} em estoque.")
                break
        else:
            print(f"Produto: {nomeproduto} não está em estoque")
    
    def exibir_estoque(self):
        print("Estoque:")
        for produto in self.produtos:
            produto.exibir_info()