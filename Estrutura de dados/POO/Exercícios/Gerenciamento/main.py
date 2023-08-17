from produto import Produto
from estoque import Estoque

def main():
    estoque = Estoque()

    opcao = 0
    while opcao != 5:
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Atualizar Quantidade")
        print("3. Procurar Produto")
        print("4. Exibir Estoque")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade em estoque: "))
            estoque.cadastrar_produto(nome, preco, quantidade)
        elif opcao == 2:
            nome_produto = input("Nome do produto: ")
            nova_quantidade = int(input("Nova quantidade em estoque: "))
            estoque.atualizar_quantidade(nome_produto, nova_quantidade)
        elif opcao == 3:
            estoque.procurar_produto()
        elif opcao == 4:
            estoque.exibir_estoque()
        elif opcao == 5:
            print("Saindo...")
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()

