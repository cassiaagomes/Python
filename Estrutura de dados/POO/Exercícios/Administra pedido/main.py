from produto import Produto
from pedido import Pedido
from sistemapedidos import SistemaPedidos

def exibir_menu():
    print("\nMenu de Pedidos:")
    print("1. Adicionar Pedido")
    print("2. Exibir Pedidos")
    print("3. Cadastrar Produto")
    print("4. Calcular Valor Total de um Pedido")
    print("5. Sair")

def main():
    sistema_pedidos = SistemaPedidos()

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cliente = input("Nome do cliente: ")
            num_itens = int(input("Número de itens no pedido: "))
            itens = []
            for _ in range(num_itens):
                nome_produto = input("Nome do produto: ")
                preco_produto = float(input("Preço do produto: "))
                quantidade = int(input("Quantidade: "))
                produto = Produto(nome_produto, preco_produto, quantidade)
                itens.append(produto)
            
            pedido = Pedido(cliente, itens)
            sistema_pedidos.adicionar_pedidos(pedido)
            print("Pedido adicionado com sucesso!")
        
        elif opcao == 2:
            sistema_pedidos.exibir_pedidos()
        
        elif opcao == 3:
            nome_produto = input("Nome do produto: ")
            preco_produto = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade em estoque: "))
            sistema_pedidos.cadastrar_produto(nome_produto, preco_produto, quantidade)
            print("Produto cadastrado com sucesso!")
        
        elif opcao == 4:
            num_pedido = int(input("Número do pedido: "))
            if num_pedido < 1 or num_pedido > len(sistema_pedidos.pedidos):
                print("Pedido não encontrado.")
            else:
                pedido = sistema_pedidos.pedidos[num_pedido - 1]
                valor_total = sistema_pedidos.calcular_valor_total(pedido)
                print(f"Valor total do pedido {num_pedido}: R$ {valor_total:.2f}")
        
        elif opcao == 5:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
