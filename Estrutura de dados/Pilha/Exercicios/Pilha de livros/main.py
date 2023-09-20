from livros import Pilha  # Substitua 'suaclasspilha' pelo nome real do arquivo onde está a classe Pilha

def exibir_menu():
    print("\nBem-vindo à Estante de Livros!")
    print("Opções:")
    print("1. Adicionar um novo livro")
    print("2. Retirar um livro")
    print("3. Verificar o livro no topo")
    print("4. Sair do programa")

def main():
    pilha_livros = Pilha() 

    while True:
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            titulo = input("Digite o título do livro a ser adicionado: ")
            pilha_livros.inserir(titulo)
            print(f"'{titulo}' foi adicionado à estante.")

        elif opcao == 2:
            try:
                livro_removido = pilha_livros.remover()
                print(f"'{livro_removido}' foi retirado da estante.")
            except IndexError:
                print("A estante de livros está vazia.")

        elif opcao == 3:
            try:
                livro_topo = pilha_livros.observar()
                print(f"O livro no topo da estante é '{livro_topo}'.")
            except IndexError:
                print("A estante de livros está vazia.")

        elif opcao == 4:
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
