import socket
from colorama import Fore, Style
from time import sleep
import threading
import random
import string
from threading import *
from interface import *
from cliente import *
from sala import *
from ed_arvoreAVLarmazenarCodigos import *
from ed_hashTableEncadeadaCliente import *
from ed_hashTableEncadeadaSalas import * 
from ed_filaEncadeadaAcoes import *




# 1- O servidor é iniciado e aguarda por conexões de clientes.
# 2- Quando um cliente se conecta, o servidor aceita a conexão e cria uma nova thread para lidar
#  com esse cliente.
# 3 - A nova thread chama a função processar_requisicao() para processar as requisições do cliente.
# 4 -O servidor continua aguardando por novas conexões,
#  enquanto as threads já criadas executam o processamento das requisições dos respectivos clientes.

class Servidor:
    def __init__(self, host, port): 
        self.__host = host # O ip host
        self.__port = port # A porta 
        self.__sock = None # O sock 
        self.__fila_acoes = Fila() # Fila que armazena as ações dos usuários .
        self.__TabelaHashSalas = ChainHashTable(10) # HashTableEncadeada que armazena as Salas criadas.
        self.__TabelaHashCliente = ChainHashTable1(11) # HashTableEncadeada que armazena conexões feitas.
        self.__ArvoreAvl = AVLTree() # Arvore AVL que busca e inseri códigos de cada sala criada. 
        



    def iniciar_servidor(self):
        
            self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criação do objeto de soquete
            self.__sock.bind((self.__host, self.__port)) # Associa o soquete ao endereço de host e porta
            self.__sock.listen(10) # Habilita o soquete para aceitar conexões, com um limite de 5 conexões em espera
            menu = Interface()
            menu.inicio_servidor(self.__host,self.__port)



            thread_exibicao = threading.Thread(target=self.mostrar_acoes)
            
            thread_exibicao.start()
            
            while True:
                conn, addr = self.__sock.accept()
                codigo = addr
                endereco_string = ":".join(map(str, codigo))
            
                self.__TabelaHashCliente.put(endereco_string, conn) 
            

                # Aceita uma conexão de um cliente
                #print(f"Conexão estabelecida com {addr}") #addr ->  Essa variável armazena informações sobre o endereço do cliente que se conectou ao servidor.
                # Normalmente, addr contém uma tupla com o endereço IP e o número da porta do cliente.
                # conn -> Essa variável representa o objeto de conexão com o cliente. É por meio desse objeto que o servidor poderá enviar e receber dados do cliente conectado.
                # O objeto conn permite a comunicação bidirecional entre o servidor e o cliente.

                # Inicia uma nova thread para lidar com a conexão do cliente
                thread = threading.Thread(target=self.__processar_requisicao, args=(conn,endereco_string))
                thread.start()
                
                
    

    def __receber_comando(self, conn):
        # Recebe os comandos dos clientes

        dados = conn.recv(1024).decode()
    
        if not dados:
            return None
        return dados 
    
    
    def __enviar_resposta(self, conn, resposta):
        #
        conn.sendall(resposta.encode())
    


    def __processar_requisicao(self, conn,endereco_string):

         
        local = ''
        try:
            while True:
            
                mensagem = self.__receber_comando(conn)
                  # Recebe uma mensagem do cliente
                
                

                
                
                
                if not mensagem:  #CADASTRAR:gabriel #CADASTRAR / NOME 
                    break

                partes = mensagem.split(':', 4)  # Divide a mensagem em três partes no máximo
                comando = partes[0]
                dado1 = partes[1] if len(partes) >= 2 else '' # Se houver pelo menos duas partes, a segunda parte é atribuída à variável dados0.
                dado2 = partes[2] if len(partes) >= 3 else '' # Se houver pelo menos três partes, a terceira parte é atribuída à variável dados1.
                dado3 = partes[3] if len(partes) >= 4 else "" # Se houver pelo menos quatro partes, a quarta parte é atribuída à variável dados2.
                dado4 = partes[4] if len(partes) >= 5 else ""
                dado5 = partes[5] if len(partes) >= 6 else ""
                



                if comando == 'CADASTRAR_USUARIO':  # Se o comando for "CADASTRAR"
                    resposta = self.__cadastrar_usuario(dado1,dado2)  # Chama o m  étodo cadastrar_usuario com os dados
                    self.__enviar_resposta(conn, resposta)
                    if resposta == '+104': #Cadastro realizado com sucesso
                        self.__fila_acoes.enfileira(f'Novo usuário cadastrado: {dado1}')  # Adicionando a ação na fila

                elif comando == 'CONSULTAR_NOME':
                    resposta = self.__consultar_nome(dado1)
                    self.__enviar_resposta(conn,resposta)
                    

                
                elif comando == 'VERIFICAR_USUARIO':
                    resposta = self.verificar_usuario(dado1,dado2)
                    self.__enviar_resposta(conn,resposta)
                    
                
                elif comando =='VERIFICAR_LOGIN':
                    resposta = self.__verificar_login(dado1,dado2)
                    self.__enviar_resposta(conn,resposta)
                    if resposta == '+105': #+Logado com sucesso
                        self.__fila_acoes.enfileira(f'{Fore.GREEN}Usuário {dado1} está logado !{Style.RESET_ALL}')
                                      
                elif comando == 'ENCERRAR_SESSAO':  
                    self.__fila_acoes.enfileira(f'{Fore.RED}Usuário {dado3} deslogou !{Style.RESET_ALL}')
                    removee = (dado1 + ':' + dado2)
                    resposta = self.__encerrar_sessao(removee)
                    self.__enviar_resposta(conn,resposta)
                    
                
                elif comando == 'SAIR_PROGRAMA':
                    removeee = (dado1 + ':' + dado2)
                    resposta = self.__encerrar_programa(removeee)
                    self.__enviar_resposta(conn,resposta)

                    
                elif comando == 'ADICIONAR_CONTATO':
                    resposta = self.__adicionar_contato(dado1,dado2)
                    
                    self.__enviar_resposta(conn,resposta)
                   
                
                    self.__fila_acoes.enfileira(f'{Fore.GREEN}No arquivo {dado1} foi adicionado o contato {dado2}.{Style.RESET_ALL}')
                    
                elif comando == 'VERIFICAR_AMIGO_ADICIONADO':
                    
                    resposta = self.__verificar_amigo_adicionado(dado1,dado2)
                    
                    print(resposta)
                    self.__enviar_resposta(conn,resposta)



                elif comando == 'LISTAR_CONTATOS':
                    resposta = self.__listar_contatos(dado1)
                    self.__enviar_resposta(conn,resposta)

                elif comando == 'CONSULTAR_USUARIO':
                    resposta = self.__consultar_usuario(dado1)
                    self.__enviar_resposta(conn,resposta)
                
                elif comando == 'CRIAR_SALA':
                    resposta = self.__criar_sala(dado1,dado2)
                    self.__enviar_resposta(conn,resposta) 
                    self.__fila_acoes.enfileira(f'{Fore.GREEN}Usuário {dado1} criou sala com o nome {dado2}.{Style.RESET_ALL}')
                    

                elif comando == 'MOSTRAR_SALAS':
                    resposta = self.__mostrar_salas()
                    self.__enviar_resposta(conn,resposta)

                elif comando == 'VERIFICAR_SALA':
                    resposta = self.__verificar_sala(dado1)
                    self.__enviar_resposta(conn,resposta)

                elif comando == 'CONSULTAR_CODIGO_CONEXAO':
                    resposta = endereco_string
                    self.__enviar_resposta(conn,resposta)

                elif comando == 'ENTRAR_NA_SALA': 
                    juncao = (dado3 + ':' + dado4) #codigo_sala / #nome_pessoa / #codigo_conexao
                    resposta = self.__entrar_sala(dado1,dado2,juncao)
                    self.__enviar_resposta(conn,resposta)

                elif comando == 'ENVIAR_MENSAGEM_SALA':
                    opa = (dado4 + ':' + dado5)
                    resposta = self.__enviar_mensagem_sala(dado1,dado2,dado3,opa)
                    self.__enviar_resposta(conn,resposta)

                elif comando == 'REMOVER_AMIGO':
                    resposta = self.__remover_amigo(dado1, dado2)
                    print(resposta)
                    self.__enviar_resposta(conn, resposta)
                
                else:
                    resposta = f'{Fore.RED}+600{Style.RESET_ALL} - Comando inválido' # Se o comando for inválido, define uma resposta padrão
                    self.__enviar_resposta(conn,resposta)
                
        except ConnectionResetError:
            print(f'Conexão encerrada pelo usuário')

        finally:
    
            self.encerrarProcessarRequisicao = True
            conn.close()
     



    def mostrar_acoes(self):
        mensagem = False  # Variável para controlar se o cabeçalho já foi impresso
        print('Ações dos usuários:')
        while True:
            while not self.__fila_acoes.estaVazia():
                if not mensagem:
                    mensagem = False
                    #print(self.__fila_acoes)
                    sleep(2)
                    acao = self.__fila_acoes.desenfileira()

                    print(f'{acao}')
             # Reinicia a variável para que o cabeçalho seja impresso novamente se houver novas ações
                    time.sleep(2)  # Aguarda 5 segundo antes de verificar a fila novamente
                    


    def __consultar_nome(self, nome):
        with open('usuarios.txt', 'r') as file:
            usuarios = file.read().splitlines()

        for usuario in usuarios:
            nome_salvo = usuario.strip().split(',')
            if nome_salvo[0] == nome:
                return f'-601' # Usuário já existente
    
        return f'+102' # Nome de usuário disponível
    

    def __consultar_usuario(self, nome):
        with Semaphore(1):
            with open('usuarios.txt', 'r') as file:
                usuarios = file.read().splitlines()

            for usuario in usuarios:
                nome_salvo = usuario.strip().split(',')
                if nome_salvo[0] == nome:
                    return f'+103'  # Usuário cadastrado
        
            return f'-602'  # Usuário inexistente
    

    def __cadastrar_usuario(self, nome,senha): #10 #gabriel #heitor #cassia #marcos 
    
       
       with Semaphore(1):
        try:

            with open('usuarios.txt', 'r') as file__read:
                usuarios = file__read.read().splitlines()
               
                    
            for usuario in usuarios:
                nome_salvo= usuario.strip().split(',')
                if nome_salvo[0] == nome:
                        return f'-601'  # +Usuário já existente.

            
            with open('usuarios.txt', 'a') as file_append:
                file_append.write(f'{nome},{senha}\n') 
                self.criar_lista(nome)
                return (f"{'+104'}")  # Cadastro realizado com sucesso

            
        except Exception as e:
            # Lidar com a exceção e retornar uma resposta adequada
            return (f'{Fore.RED}-603{str(e)}')  # Erro durante o cadastro:
        

    def __verificar_login(self, nome_usuario, senha):
     with open('usuarios.txt', 'r') as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            if len(partes) == 2:
                nome, senha_registrada = partes
                if nome == nome_usuario and senha == senha_registrada:
                    return '+105'  # +Logado com sucesso
            else:
                # Lidar com o caso em que a linha não possui duas partes separadas por vírgula
                return '-604'  # -Erro na formatação da linha

     return '-605' # -Erro na senha ou no usuário
    

    def __verificar_amigo_adicionado(self, nome_usuario,nome_amigo): 
        arquivo = f'c-{nome_usuario}.txt'
        #try:
        with open(arquivo, 'r') as f:
            for linha in f:
                if nome_amigo in linha:
                    return f'-606'  #Já existe esse nome na lista de contatos
        
    
        return '+106'  #Não existe esse nome na lista de contatos


    def __listar_contatos(self, nome_usuario):
        arquivo = f"c-{nome_usuario}.txt"
        try:
            with open(arquivo, 'r') as contatos_file:
                contatos = contatos_file.readlines()
            
            if not contatos:
                return f"{Fore.RED}Lista de contatos vazia{Style.RESET_ALL}"
            else:
                return f"{Fore.GREEN}Lista de contatos:\n" + "".join(contatos)
        
        except IOError as e:
            return f"{Fore.RED}Erro ao acessar o arquivo{Style.RESET_ALL}"


    def __remover_amigo(self, nome_usuario, nome_amigo):
        arquivo = f"c-{nome_usuario}.txt"
        consulta = self.__verificar_amigo_adicionado(nome_usuario,nome_amigo)

        if consulta == '-606':

            with open(arquivo, 'r') as f:
                linhas = f.readlines()
            
            with open(arquivo, 'w') as f:
                for linha in linhas:
                    if nome_amigo.strip() != linha.strip():
                        f.write(linha)

            return '+108'

        else: 
            return '-632'
    

    def criar_lista(self,nome_usuario):
        with open (f'c-{nome_usuario}.txt', 'w') as file :
            return
    

    def __adicionar_contato(self,nome_arquivo,contato):
        with open(nome_arquivo, 'a') as contatos_file:
            contatos_file.write(contato + '\n')
        return f'+107'  # Contato adicionado com sucesso.
    

    
    
    
    
    

    def __verificar_sala(self,codigo):
        if  self.__TabelaHashSalas.search(codigo):
            return f'+120'
        
        else:
            return f'-620'
        
    
    def gerar_codigo_aleatorio(self):
        caracteres = string.ascii_letters + string.digits
        codigo = ''.join(random.choices(caracteres, k=10))
        return codigo
    

    def __encerrar_sessao(self,codigo):
        teste = self.__TabelaHashCliente.remove(codigo)
        sleep(2)
        return f'+160' #Sessão finalizada
   
    
    def __encerrar_programa(self,codigo):
        teste = self.__TabelaHashCliente.remove(codigo)
        sleep(2)
        return f'+130'
                    


    
    def __criar_sala(self,usuario,nome_sala):
        codigo = self.gerar_codigo_aleatorio()
        
        while self.__ArvoreAvl.busca(codigo):
            codigo = self.gerar_codigo_aleatorio()
        self.__ArvoreAvl.insert(codigo)

        adicionar = Sala(nome_sala,codigo,usuario)
        armazenar = self.__TabelaHashSalas.put(codigo,adicionar)               
        return f'{Fore.GREEN}+171,{codigo}{Style.RESET_ALL}'
    
    #entrar na sala
    def __entrar_sala(self,codigo_sala,nome_pessoa,codigo_conexao): 
        nome = nome_pessoa
        participante = self.__TabelaHashCliente.get(codigo_conexao) #clientes conectados no server
        sala = self.__TabelaHashSalas.get(codigo_sala)  # Salas no serves
        verificar = sala.add(participante) # Adicionando cliente em uma sala
        if verificar == 'Deu bom':
            
            return f'+150' 
        else:
            return f'-650'   
    #enviar mensagem
    def __enviar_mensagem_sala(self, nome, mensagem, codigo_sala,codigo_conexao):
        
        sala = self.__TabelaHashSalas.get(codigo_sala) 
        
        
        objetos_participantes = sala.retornar_participantes() 

        if mensagem != 'SAIR':
            envio = f'{nome}:{mensagem}'
            for participante in objetos_participantes:
                    self.__enviar_resposta(participante, envio)
            return f'Mensagem enviada!'
        else:
            participante = self.__TabelaHashCliente.get(codigo_conexao)
            print(participante)
            sala = self.__TabelaHashSalas.get(codigo_sala)
            print(sala)
            verificar = sala.remover(participante)
            codigo_conexao.close()
            


            if verificar == 'Deu bom':
                return 'SAIR'
            else:
                return 'Deu erro'
           
    
    def resgatar_informacoes(self):
        socket.gethostname()
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        print(f'Este é o IP do servidor: {ip_address}')

            

    


        
        
        

        







    





    

    

    
    
      
    
    




    


    
    

serve1 = Servidor('0.0.0.0',5000)

serve1.resgatar_informacoes() 
serve1.iniciar_servidor() 
 


#return "+201"  # Nome de usuário já existente
#return "+101"  # Cadastro realizado com sucesso#X'1