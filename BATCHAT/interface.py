from colorama import Fore, Style
import os
import time
import threading
from time import sleep


class Interface:
    def __init__(self, tam=52):
        self.__tamanho_linha = tam

    def linha(self):
        return '~' * self.__tamanho_linha

    def inicio(self, txt):
        print(self.linha())
        print(f"{Fore.YELLOW}{txt.center(self.__tamanho_linha)}{Style.RESET_ALL}")
        print(self.linha())

    def menu(self, lista):
        self.inicio('MENU INICIAL')
        for i in lista:
            print(f'{i}')
        print(self.linha())
    
    


    def executarMenu(self):  
        self.inicio('''
            ⠀⠀⠀⠀⠀⠀⢀⣀⡠⠤⠤⠴⠶⠶⠶⠶⠦⠤⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣠⠖⢛⣩⣤⠂⠀⠀⠀⣶⡀⢀⣶⠀⠀⠀⠐⣤⣍⡛⠲⣄⠀⠀⠀⠀
            ⢀⡴⢋⣴⣾⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⣿⣿⣿⣷⣦⡙⢦⡀⠀
            ⡞⢠⣿⣿⣿⣿⣿⣿⣷⣤⣤⣴⣿⣿⣿⣿⣦⣤⣤⣾⣿⣿⣿⣿⣿⣿⡆⢳⠀
            ⡁⢻⣿⣿⣿⣿⣿⣿⣿⣿ BATCHAT ⣿⣿⣿⣿⣿⣿⣿⣿⡿⢈⠆
            ⢧⡈⢿⣿⣿⣿⠿⠿⣿⡿⠿⠿⣿⣿⣿⣿⠿⠿⢿⣿⠿⠿⣿⣿⣿⡿⢁⡼⠀
            ⠀⠳⢄⡙⠿⣇⠀⠀⠈⠁⠀⠀⠈⢿⡿⠁⠀⠀⠈⠁⠀⠀⣸⠿⢋⡠⠞⠀⠀
            ⠀⠀⠀⠉⠲⢤⣀⡀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⢀⣀⡤⠖⠉⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠈⠉⠉⠐⠒⠒⠒⠒⠒⠒⠒⠒⠒⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀
''')
        
      

        self.menu([f"{Fore.BLUE}1. Cadastrar{Style.RESET_ALL}", f"{Fore.GREEN}2. Entrar{Style.RESET_ALL}", f'{Fore.RED}3. Sair{Style.RESET_ALL}'])
        
    

    def limpar_tela(self):
        if os.name == 'nt':  # Verificar se o sistema operacional é Windows
            os.system('cls')
        else:
            os.system('clear')



    def inicio_servidor(self,a,b):
        print(f"{Fore.GREEN} Servidor inicializado com sucesso !")
        sleep(2)
        sleep(2)
        print(f' {Fore.GREEN}Aguardando clientes no servidor do BATCHAT!.')
        sleep(2)
        print(f"{Fore.GREEN} Aguardando conexões no host: {a} e na porta:{b}...{Style.RESET_ALL}")

    
    def menu2(self):

        print(f'''{Fore.GREEN}[1] Adicionar contato{Style.RESET_ALL}
{Fore.RED}[2] Remover contato{Style.RESET_ALL}
{Fore.YELLOW}[3] Listar contato{Style.RESET_ALL}
{Fore.GREEN}[4] Criar sala{Style.RESET_ALL}
{Fore.GREEN}[5] Entrar em uma sala{Style.RESET_ALL}
{Fore.RED}[6] Logout{Style.RESET_ALL}''')
        print()
            
                