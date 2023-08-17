import socket
from interface import Interface
import os
from time import sleep
from colorama import Fore, Style
from pyfiglet import figlet_format
from threading import Semaphore
from interface import Interface
import threading



class Cliente:
    def __init__(self, host, port):

        ''' Inicialização das propriedades da classe Cliente '''

        # Armazena o host para a conexão obrigado
        self.__host = host  

        # Armazena a porta para a conexão
        self.__port = port  

        # Inicialmente, o objeto de socket é None
        self.__sock = None  

        # Instancia um objeto da classe Interface para acesso à interface do usuário
        self.__interface = Interface()    

        # O nome do usuário é inicialmente None
        self.__nome_usuario = None     

        # O IP/PORTA antes dele logar
        self.__codigo_conexao_fora = None
        
        # O IP/PORTA depois dele logar
        self.__codigo_conexao_dentro = None  

        
        self.__encerrar_thread = threading.Event()




       


    def conectar(self):
            '''
            Método responsável por criar um objeto socket 

            Estabelece uma conexão com o servidor

            '''
            
            # Criação do objeto de soquete com protocolo de transporte TCP/IP
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # # Estabelece a conexão com o servidor usando o endereço do host e o número da porta fornecidos
            self.__sock.connect((self.__host, self.__port))
            # thread_enviar  = threading.Thread(target=self.enviar_comando,args=(comando))
            # thread_enviar.start()

    #recebimento de mensagens no chat
    def receber_mensagem_sala(self): 
        evento_encerrar = threading.Event()
        while not self.__encerrar_thread.is_set():
            dados = self.__sock.recv(1024).decode()
            if not dados:  # Verifica se não há mais dados recebidos
                break
            print(dados)
            if dados ==f'{self.__nome_usuario}:sair':
                evento_encerrar.set()
                break

    #envia mensagens para o chat    
    def enviar_mensagem_sala(self,mensagem):
        self.__sock.sendall(mensagem.encode())


    def __str__(self) -> str:
        return f'{self.__codigo_conexao_fora}'
              
            
    def __enviar_comando(self,comando):
        '''
        Método responsável por enviar um comando ao servidor

        Recebe  como parâmetro

        '''
        
        # É enviado um comando para o servidor, e a partir dele, será executada uma ação.
        self.__sock.sendall(comando.encode()) 


    def __receber_resposta(self): 
        '''
        é responsável por receber a 

        resposta do servidor. 
        '''

        # Recebe a resposta a servidor.
        dados = self.__sock.recv(1024).decode() 
        return dados
    

    def __consultar_usuario(self,nome):
        '''
        método responsável por enviar uma solicitação
        
        de consulta de usuário para o servidor

        e aguardar a resposta

        '''

        # Loop infinito para realizar a consulta até obter um resultado
        while True:  

            # Monta o comando de consulta com o nome do usuário
            comando = f'CONSULTAR_NOME:{nome}' 
             
            # Envia o comando para o servidor
            self.__enviar_comando(comando)        

            # Aguarda a resposta do servidor
            resultado = self.__receber_resposta()  
            
            # Retorna o resultado da consulta
            return resultado                     


    def cadastrar_usuario(self):
        '''
        Método para implementar a função

        de cadastro do usuário

        solicitando nome e senha para o cadastro
        
        '''

        # Imprime o título "CADASTRO" estilizado na tela
        print(figlet_format('CADASTRO', font='slant'))  

        # Loop principal para o cadastro do usuário
        while True:             
            sair = str  
            
            # Loop para obter a opção de sair ou continuar {Fore.BLUE}{Style.RESET_ALL}
            while sair != 'n' and sair != 's':

                # Solicita a entrada do usuário
                sair = input(f'{Fore.BLUE}Deseja retornar ao menu inicial?[S/N]{Style.RESET_ALL}').lower()
                
            self.__interface.limpar_tela()
            # Se o usuário deseja sair, encerra o loop
            
            if sair == 's':
                break

            # Solicita o nome de usuário ao usuário
            nome = input(f'{Fore.YELLOW}Digite um nome de usuário: {Style.RESET_ALL}') 

            # Consulta o servidor para verificar a disponibilidade do nome de usuário
            resposta = self.__consultar_usuario(nome)
            
            
            
            

             # Verifica se o nome de usuário atende aos critérios
            if len(nome) > 0 and len(nome) <= 8 and nome.isalnum() and resposta == '+102': #+Nome de usuário disponível
                sleep(1)
                self.__interface.limpar_tela()

                # Imprime a mensagem de nome de usuário disponível
                print(f'{Fore.GREEN}{resposta}{Style.RESET_ALL}')
                break
            
            # Verifica se o nome de usuário já existe
            if len(nome) > 0 and len(nome) <= 8 and nome.isalnum() and resposta == '-601': #Usuário já existente
                sleep(1)
                self.__interface.limpar_tela()

                # Imprime a mensagem de usuário já existente
                print(f'{Fore.RED}{resposta}{Style.RESET_ALL}')
                sleep(2)
                self.__interface.limpar_tela()
            
            # Verifica se o nome de usuário não atende aos critérios
            if len(nome) == 0 or len(nome) > 8 or nome.isalnum() == False:
                print('O nome deve conter no máximo 8 caracteres e ser composto apenas por letras e números.')
                sleep(2)
                self.__interface.limpar_tela()
        

        # Se o usuário optou por continuar o cadastro
        sleep(2)
        self.__interface.limpar_tela()
        if sair == 'n':    
            while True:

                # Solicita a senha ao usuário
                senha = input(f'{Fore.YELLOW}Dgite uma senha entre 5 a 8 dígitos:{Style.RESET_ALL}')
                cont = 0
                for i in range(len(senha)):    
                    if senha[i] == ' ' or senha[i] == ',':
                        cont += 1

                # Inicialização da variável certo
                certo = True  
                if cont >= 1:
                    certo = False
                
                # Verifica se a senha atende aos critérios
                if len(senha) >= 5 and len(senha) <= 8:
                    break
                
            # Monta o comando de cadastro com nome e senha
            comando = (f"CADASTRAR_USUARIO:{nome}:{senha}")
            
            #Envia o comando de cadastro para o servidor
            self.__enviar_comando(comando)  
            sleep(2)
            self.__interface.limpar_tela()

            #Aguarda resposta do servidor
            resposta = self.__receber_resposta()

            #Imprime a resposta do servidor
            print(f'{Fore.GREEN}{resposta}{Style.RESET_ALL}')


    def realizar_login(self):
        ''' 
        Método para solicitar as informações de login

        do usuário, enviando informações para o servidor

        e recebendo a resposta. 
        
        '''

        #LImpa a tela
        self.__interface.limpar_tela()

        #Exibe a tela de login
        self.__interface.inicio('LOGIN')

        #Loop infinito para solicitar as informações de login
        while True:

            #Variável para armazenar a opção de retorno
            sair = str

            #Loop para solicitar ao usuário se deseja retornar ao menu inicial
            while sair != 'n' and sair != 's':
                sair = input(f'{Fore.BLUE}Deseja retornar ao menu inicial?[S/N]{Style.RESET_ALL} ').lower()
                self.__interface.limpar_tela()

            # Se a opção for 's' (sim), limpa a tela e retorna ao menu
            if sair == 's':
                self.__interface.limpar_tela()
                return None

            #Solicita o nome de usuário cadastrado
            nome_usuario = input(f'{Fore.YELLOW}Nome de usuário:{Style.RESET_ALL} ')

            #Solicita a senha
            senha = input(f'{Fore.YELLOW}Senha:{Style.RESET_ALL} ')

            #Monta o comando de verificação do login
            comando = (f'VERIFICAR_LOGIN:{nome_usuario}:{senha}')

            #Envia o comando para o servidor
            self.__enviar_comando(comando)

            #Aguarda 2 segundos
            sleep(2)

            #Limpa a tela
            self.__interface.limpar_tela()

            #Recebe a resposta do servidor
            resposta = self.__receber_resposta()

            if resposta != '-605':
                print(f'{Fore.GREEN}{resposta}{Style.RESET_ALL}')
                sleep(2)
                self.__interface.limpar_tela()
            else:
                print(f'{Fore.RED}{resposta}{Style.RESET_ALL}')
                sleep(2)
                self.__interface.limpar_tela()

            #Se a resposta do servidor for '+105'
            if resposta == '+105': 

                #O nome é armazenado
                self.__nome_usuario = nome_usuario
                

                codigo_conexao_dentro =f'CONSULTAR_CODIGO_CONEXAO'
                self.__enviar_comando(codigo_conexao_dentro)
                codigo_conexao1 = self.__receber_resposta()
                self.__codigo_conexao_dentro = codigo_conexao1
                self.__codigo_conexao_fora = self.__codigo_conexao_dentro
                sleep(3)
                break
        
        
        return resposta
 
           
    def encerrar_programa(self):
        '''
        Função que limpa a tela do cliente e fecha o socket dele
        '''
        #conexao = self.codigo_conexao_fora
        try:
            # Limpa a tela do cliente 
            consulta = 'CONSULTAR_CODIGO_CONEXAO'
            self.__enviar_comando(consulta)
            resposta = self.__receber_resposta()

            enviar = f'SAIR_PROGRAMA:{resposta}'
            self.__enviar_comando(enviar)
            encerrar = self.__receber_resposta()
            
            


            # Chama a função close do sock, e fecha a conexão com o servidor
            self.__sock.close()

            # Sinaliza ao usuário que está fechando
            print(f'{Fore.GREEN}{encerrar}{Style.RESET_ALL}')

            # Realiza uma espera de 2 segundos como efeito visual
            sleep(2)

            # Limpa a tela do cliente
            self.__interface.limpar_tela()
                

                
        # Caso dê algum erro genérico ao encerrar a aplicação, cairá nessa exceção.    
        except:
            raise Exception ('Ocorreu algum problema ao encerrar a aplicação')
        
       
    def logado(self,aviso):
        '''
        Verifica se a resposta recebida
        
        indica que o usuário está logado
        
        '''

        # Verifica se o aviso recebido indica login bem-sucedido
        if aviso == '+105': 

            # Retorna True se o aviso for +105, ou seja, logado com sucesso
            return True
        else:

            # Retorna False para qualquer outro aviso, indicando falha no login
            return False

        
    def adicionar_contato(self): 
        '''

        Permite ao usuário adicionar um contato
        
        '''

        # Obtém o nome de usuário do cliente
        nome_usuario = self.__nome_usuario

        # Define o nome do arquivo de contatos do usuário
        nome_arquivo = f'c-{nome_usuario}.txt' 

        #Loop principal do método
        while True:
            sair = str
            while sair != 'n' and sair != 's':

                # Verifica se o usuário deseja retornar ao menu inicial
                sair = input(f'{Fore.BLUE}Deseja retornar ao menu inicial?[S/N] {Style.RESET_ALL}').lower()
                self.__interface.limpar_tela()
                sleep(3)

            # Se sair for == 's'(sim) o usuário deseja retorna ao menu inicial
            if sair == 's':
                self.__interface.limpar_tela()
                sleep(3)
                break

            # Solicita ao usuário o nome do contato a ser adicionado
            contato = input(f'{Fore.YELLOW}Digite o nome do contato: {Style.RESET_ALL}') 
            self.__interface.limpar_tela()
            sleep(3)

            # Envia o comando para consultar se o usuário existe
            comando = self.__enviar_comando(f'CONSULTAR_USUARIO:{contato}') # ->
            
            # Recebe a resposta do servidor
            resposta = self.__receber_resposta()
            
            # print(resposta)
            # sleep(10)


            #Se o usuário não existe, a resposta recebida é '-602'
            if resposta == '-602': #Usuário inexistente
                print(f'{Fore.RED}{resposta}{Style.RESET_ALL}')
                sleep(3)
                self.__interface.limpar_tela()
            
            else:
                
                #Condição para verificar se o contato adicionado não é o prórpio usuari
                if contato != nome_usuario:

                    #Verifica se o contato já foi adicionado anteriormente
                    comando2 = self.__enviar_comando(f'VERIFICAR_AMIGO_ADICIONADO:{nome_usuario}:{contato}') #ok
                    
                    #Recebe a resposta do servidor
                    resposta2 = self.__receber_resposta() 
                    
                    #Se o contato não foi adicionado a lista de contatos
                    if resposta2 == '+106': #Não existe esse nome na lista de contatos
                        
                        #É enviado um comando para o servidor adionar o contato
                        comando3 = self.__enviar_comando(f'ADICIONAR_CONTATO:{nome_arquivo}:{contato}')
                        
                        #Recebe a resposta do servidor
                        resposta_serv = self.__receber_resposta()
                        print(f'{Fore.GREEN}{resposta_serv}{Style.RESET_ALL}')
                        # print('Contato adicionado com sucesso!')
                        sleep(2)
                        self.__interface.limpar_tela()
                        break
                                    
                    else:

                        #Informa que o contato já existe na lista
                        
                        print(f'{Fore.RED}-606{Style.RESET_ALL}') 
                        sleep(2)
                        self.__interface.limpar_tela()
                else:

                    #Não é possível adicionar o proprio usuário
                    print(f'{Fore.RED}-610{Style.RESET_ALL}')
                    sleep(2)
                    self.__interface.limpar_tela()


    def listar_contatos(self):
        '''
        Método responsável por obter a lista de contatos
        
        e exibir-la
        '''

        # Envia o comando para obter a lista de contatos do usuário
        comando = self.__enviar_comando(f'LISTAR_CONTATOS:{self.__nome_usuario}')
        
        # Recebe a resposta do servidor contendo a lista de contatos
        resposta = self.__receber_resposta()

        #Exibe a lista de contatos
        print(resposta)
        sleep(5)
        self.__interface.limpar_tela()
        #Aguarda por 2 segundos


    def criar_sala(self):
        # Cria salas
        usuario = self.__nome_usuario
        sair = str
        while sair != 'n' and sair != 's':
            # Verifica se o usuário deseja retornar ao menu inicial
            sair = input(f'{Fore.BLUE}Deseja retornar ao menu inicial?[S/N]{Style.RESET_ALL} ').lower()
            self.__interface.limpar_tela()
            sleep(3)
        # Se sair for == 's'(sim) o usuário deseja retorna ao menu inicial
            if sair == 's':
                self.__interface.limpar_tela()
                sleep(3)
                break
        #criação da sala
        if sair == 'n':
            while True:
                nome_sala = input(f'{Fore.YELLOW}Digite o nome da sala a ser criada: {Style.RESET_ALL}')
                self.__interface.limpar_tela()
                #validação para um nome alfanumérico
                if nome_sala.isalnum():
                    break
                else:
                    print(f'{Fore.RED}Só é aceito números e letras para formar o nome da sala{Style.RESET_ALL}')
                    sleep(2)
                    self.__interface.limpar_tela()
            
            comando = f'CRIAR_SALA:{usuario}:{nome_sala}'
            self.__interface.limpar_tela()
    
            self.__enviar_comando(comando)
            
            #recebimento da resposta do servidor
            resposta = self.__receber_resposta()
            

            print(resposta)
            sleep(15)
            self.__interface.limpar_tela()

            return

    
    #entrar na sala
    def entrar_sala(self):
        nome = self.__nome_usuario
    
        #envio de requisição para a verificação de existência da sala
        codigo = input(f'{Fore.YELLOW}Digite o código da sala:{Style.RESET_ALL} ')
        sleep(2)
        self.__interface.limpar_tela()
        codigo1 = f'VERIFICAR_SALA:{codigo}'
        self.__enviar_comando(codigo1) 
        #resposta do servidor
        codigo2 =self.__receber_resposta()
        if codigo2 == '-620':
            print(f'{Fore.RED}{codigo2}{Style.RESET_ALL}')
        
        else:
            
            sleep(2)
            self.__interface.limpar_tela()
            adicionar_na_sala = f'ENTRAR_NA_SALA:{codigo}:{nome}:{self.__codigo_conexao_dentro}'
            self.__enviar_comando(adicionar_na_sala)
            #recebimento de resposta do servidor
            resposta = self.__receber_resposta()
            if resposta == '+150':
                print(f'{Fore.GREEN}{resposta}{Style.RESET_ALL}')
                sleep(2)
                self.__interface.limpar_tela()
                #inicialização da thread para o envio de mensagens
                thread_receber_mensagem = threading.Thread(target=self.receber_mensagem_sala)
                thread_receber_mensagem.start()
                mensagem = ''

                while mensagem != 'sair':
    
                    mensagem = input('')
                    #requisição para o envio da mensagem do chat para o servidor
                    mensagem1 = f'ENVIAR_MENSAGEM_SALA:{nome}:{mensagem}:{codigo}:{self.__codigo_conexao_dentro}'
                    self.__enviar_comando(mensagem1)
                  
                    mensagem2 = self.__receber_resposta()
                    #condição para mostrar apenas mensagens diferentes da mensagem usada como comando para sair do chat
                    
                    if mensagem2 == 'sair':
                        print(mensagem2)
                        break
          

    #método para logout
    def encerrar_sessao(self):
        usuario = self.__nome_usuario

        #envio de requisição para fazer logout
        comando = self.__enviar_comando(f'ENCERRAR_SESSAO:{self.__codigo_conexao_dentro}:{usuario}')
        #recebimento de resposta do servidor
        resposta = self.__receber_resposta()
        #codição para fazer logout
        if resposta == '+160':
            print(f'{Fore.GREEN}{resposta}{Style.RESET_ALL}')
            sleep(2)

    #método para remoção de contato
    def remover_amigo(self):
        cliente = self.__nome_usuario 

        #Solicitar o nome do amigo
        amigo_remover= input(f'{Fore.RED}Digite o nome do amigo a ser removido:{Style.RESET_ALL} ')
        try:
            #Verificar se a conexão está estabelecida corretamente
            #Enviar comando REMOVER_AMIGO para o servidor


                comando = f'REMOVER_AMIGO:{cliente}:{amigo_remover}'
                comando = self.__enviar_comando(comando)

                #Receber resposta do servidor
                resposta = self.__receber_resposta()
                self.__interface.limpar_tela()
                sleep(2)
                if resposta == '+108':
                    print(f'{Fore.GREEN}{resposta}{Style.RESET_ALL}')
                
                else:
                    print(f'{Fore.RED}{resposta}{Style.RESET_ALL}')
                    
                sleep(2)
                self.__interface.limpar_tela()

        except Exception as e:
                 print(f"Ocorreu um erro")

        