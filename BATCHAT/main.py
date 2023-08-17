from cliente import Cliente
from interface import Interface
from time import sleep
from colorama import Fore, Style

class Main:
    def __init__(self,iniciar):
        self.__iniciar = iniciar

    #inicialização do programa principal
    def main(self):
        ip = input('Digite o ip pra se conectar: ')
        porta = int(input('Digite a porta para se conectar: '))
        
        while True:
           
           #ip e porta
            cliente = Cliente(ip, porta)
            
            #estabelecimento de conexão
            cliente.conectar()
            
            
            #exibição do menu
            menu = Interface()
            menu.executarMenu()
            
            #opção a ser escolhida no menu
            opcao = input(f'{Fore.YELLOW}Digite a opção desejada:{Style.RESET_ALL}')
            menu.limpar_tela()

            #cadastro de usuário
            if opcao == "1":
                menu.limpar_tela()
                cliente.cadastrar_usuario()
                sleep(2)
                menu.limpar_tela()
            
            #login
            elif opcao == "2":
                menu.limpar_tela()
                login = cliente.realizar_login ()
                sleep(2)
                menu.limpar_tela()

                #ao logar o cliente é direcionado para o segundo menu
                if cliente.logado(login):
                    while True:
        
                        #exibição do segundo menu
                        
                        menu.menu2()

                        #opção a ser escolhida no menu dois
                        opcao2 = input(f'{Fore.YELLOW}Digite a opção desejada:{Style.RESET_ALL}' )
                        print()
                        
                        #adicionar contato
                        if opcao2 == '1':
                            menu.limpar_tela()
                        
                            cliente.adicionar_contato()
                        
                        #listar contato     
                        elif opcao2 == '2':
                            menu.limpar_tela()
                            
                            
                            cliente.remover_amigo()
                            
                        #remover contato
                        elif opcao2 == '3':
                            menu.limpar_tela()
                            cliente.listar_contatos()
                        
                        #conversar com contato
                        elif opcao2 == '4':
                            menu.limpar_tela()
                            cliente.criar_sala()
                        
                        #criar sala
                        elif opcao2 == '5':
                            menu.limpar_tela()
                            cliente.entrar_sala()
                            sleep(2)
                            menu.limpar_tela()
                        
                        #salas criadas
                        elif opcao2 == '6':
                            menu.limpar_tela()
                            cliente.encerrar_sessao()
                            menu.limpar_tela()
                            break
                            
                        #sair
                        #caso a opção escolhida seja inválida
                        else:
                            menu.limpar_tela()
                            print(f"{Fore.RED} Opção inválida. Digite novamente. {Style.RESET_ALL}")
                            sleep(2)
                            menu.limpar_tela()

                        
                        

            #encerrar programa
            elif opcao == "3":
                cliente.encerrar_programa()
                break
            #caso a opção escolhida seja inválida   
            else:
                print("Opção inválida. Digite novamente.")
                menu.limpar_tela()




if __name__ == "__main__":
    main = Main('iniciar')
    main.main()







