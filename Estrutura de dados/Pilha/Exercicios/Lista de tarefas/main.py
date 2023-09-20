from Tarefas import Pilha

def exibir_menu(): 
    print("Bem-vindo ao Gerenciador de tarefas\n")
    print("1. Adicionar uma tarefa")
    print("2. Remover a ultima tarefa inserida")
    print("3. Observar tarefa no topo da pilha")
    print("4. Exibir lista de tarefas")
    print("5. Sair\n")

def main():
    pilha = Pilha()

    while True:
        exibir_menu()

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tarefa = input("Informe a tarefa a ser adicionada: ")
            pilha.inserir(tarefa)
            print(f"Tarefa {tarefa} inserida na pilha.\n")

        elif opcao == 2: 
            try:
                remover = pilha.remover()
                print(f"Tarefa {remover} removida da pilha.\n")
            except IndexError:
                print("A pilha está vazia.")

        elif opcao == 3:
            try:
                topo = pilha.topo()
                print(f"A tarefa no topo da pilha é: {topo}\n")
            except IndexError:
                print("A pilha está vazia.\n")

        elif opcao == 4:
            print(pilha)
        
        elif opcao == 5:
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
