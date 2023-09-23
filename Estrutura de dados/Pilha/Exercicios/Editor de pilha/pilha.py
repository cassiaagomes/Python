class No:
    def __init__(self, dado):
        self.dado = dado # Cria um objeto No com um atributo 'dado' e 'prox' inicializado como None
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None # Inicializa uma pilha vazia com o 'topo' apontando para None
        self.tamanho = 0 # Inicializa uma pilha com o tamanho igual a zero
    
    def __len__(self):
        return self.tamanho # Retorna o tamanho da pilha
    
    def empilhar(self, novo_dado):
        no = No(novo_dado) # Cria um novo no que recebe a nova informação do dado 
        no.prox = self.topo # O no criado, sempre vai apontar para o prox. Neste caso o prox é o topo
        self.topo = no # Atualiza o topo da pilha para ser o novo no informado
        self.tamanho += 1 # Incrementa o tamanho da pilha

    def desempilhar(self):
        if self.tamanho > 0: # Verifica se a pilha não está vazia
            no = self.topo # Armazena o nó no topo da pilha em 'nó'
            self.topo = self.topo.prox # Atualiza o topo da pilha para o próximo elemento
            self.tamanho -= 1 # Decrementa o tamanho da pilha
            return no.dado # Retorna o dado do nó removido
        else:
            raise IndexError("A sua pilha está vazia!") # Levanta uma excessão caso a pilha esteja vazia
        
    def topinho(self):
        if self.tamanho >0:
            return self.topo.dado #Retorna o dado do topo da pilha
        else:
            raise IndexError("Pilha vazia")
        
    def estah_vazia(self):
        if self.tamanho>0:
            return False
        else:
            return True
    
    def desempilhar_tudo(self):
        try:
            while self.tamanho >= 0:
                    elemento = self.desempilhar()
                    print(f"O elemento {elemento} foi desempilhado.")
        except IndexError as e:
            print(e)
    
    def inverter(self):
        pilha_aux = Pilha()
        try:
            while self.tamanho > 0:
                elemento = self.desempilhar()
                pilha_aux.empilhar(elemento)
                return pilha_aux
        except IndexError as e:
            print(e)
        
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while(ponteiro):
            r += str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.prox
        return r
    
    def __str__(self):
        return self.__repr__()
        
        

