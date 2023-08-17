class Sala:
    def __init__(self,nome,codigo,dono):
        self.__nome = nome 
        self.__codigo= codigo
        self.__nome_dono = dono 
        self.participantes = [] 
        



    @property
    def nome_sala(self):
        return self.__nome
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome_dono(self):
        return self.__nome_dono
    
    
    
    @nome_sala.setter
    def setar_nome_sala(self,nome_sala):
        self.__nome = nome_sala



    @codigo.setter
    def setar_codigo(self,codigo_sala):
        self.__codigo = codigo_sala

    @nome_dono.setter
    def setar_codigo(self,nome_dono):
        self.__nome_dono = nome_dono

        
    def __str__(self) -> str:
        return f'Nome da sala: {self.__nome}'
    

    def remover_participante(self, participante):
        self.participantes.remover_por_valor(participante)
        

    def adicionar_participante(self, participante):
        if self.participantes.appendd(participante) == 'Deu bom':
            return 'Deu bom'
        else:
            return 'Deu ruim'
    
    def add(self, participante):
        try:
            self.participantes.append(participante)
            return 'Deu bom'
        except IndexError:
            return 'Deu ruim'
        
    def retornar_participantes(self):
        return self.participantes
    
    def remover(self,participante):
        try:
            self.participantes.remove(participante)
            return 'Deu bom'
        except IndexError:
            return 'Deu ruim'

            
        
    

    
    

    

    
    


    # def mostrar_acoes(self,usuario):
    #     mensagem = False  # Variável para controlar se o cabeçalho já foi impresso
    #     print('Ações dos usuários:')
    #     while True:
    #         while not self.__fila_acoes.estaVazia():
    #             if not mensagem:
    #                 mensagem = False
    #                 #print(self.__fila_acoes)
    #                 acao = self.__fila_acoes.desenfileira()
    #                 print(f'{acao}')
    #          # Reinicia a variável para que o cabeçalho seja impresso novamente se houver novas ações
    #                 time.sleep(3)  # Aguarda 5 segundo antes de
    




    # def nome(self, nome_usuario,contato):
    #     concatenação = nome_usuario + contato
    #     if concatenação == '1':
    #         self.__nome = concatenação
    #     pass