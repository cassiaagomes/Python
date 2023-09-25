from pilha import Pilha  # Importe a classe Pilha do seu arquivo Pilha.py

def exibir_menu(pilha):
    print("\nEditor de Pilha v1.2")
    print("=====================================")
    print(f"Tamanho da pilha: {len(pilha)}")
    print("=====================================")
    print("(e) Empilhar")
    print("(d) Desempilhar")
    print("(t) Tamanho")
    print("(o) Obter elemento do topo")
    print("(p) Imprimir pilha")
    print("(z) Desempilhar tudo")
    print("(i) Inverter a pilha")
    print("(s) Sair")
    print("=====================================")

def main():
    pilha = Pilha()  # Crie uma instância da classe Pilha
    opcao = ""

    while opcao != "s":
        exibir_menu(pilha)
        opcao = input("Digite sua opção: ")

        if opcao == "e":
           novo_dado = int(input("Digite o número a ser empilhado: "))
           pilha.empilhar(novo_dado)
           print(f"Você empilhou o  número: {novo_dado}.")

        elif opcao == "d":
            questao = input(f"O número que se encontra no topo é o {pilha.topinho()}. Deseja desempilhar? [s/n] ").lower()
            if questao == "s":
                pilha.desempilhar()
                print(f"O número foi desempilhado. ")
            elif questao == "n":
                exibir_menu(pilha)
            else:
                raise IndexError("Informação inválida. Tente novamente")
            
        elif opcao == "t":
            print(len(pilha))

        elif opcao == "o":
            print(f"O topo da pilha é o número: {pilha.topinho()}")

        elif opcao == "p":
            print(pilha)
        
        elif opcao == "z":
            print("Desempilhando...")
            pilha.desempilhar_tudo()

        elif opcao == "i":
            pilha.inverter()
            print(pilha)
        

        elif opcao == "s":
            print("saindo...")
if __name__ == "__main__":
    main()
