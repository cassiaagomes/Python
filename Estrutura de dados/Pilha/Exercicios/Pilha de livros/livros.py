class No:
    def __init__(self, dado):
        self.dado = dado #Cria um objeto No com um atributo 'dado' e 'prox' inicializado com None
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None #Inicializa uma pilha vazia com 'topo' apontando para o None
        self.tamanho = 0 #Inicializa o tamanho da pilha como 0

    def __len__(self):
        return self.tamanho #Retorna o tamanho da pilha (quantidade de elementos)

    def inserir(self, novo_dado):
        no = No(novo_dado) #Cria um novo nó com o dado passado como argumento
        no.prox = self.topo #0 novo nó aponta para o antigo topo da pilha
        self.topo = no #Atualiza o topo da pilha para ser um novo nó
        self.tamanho += 1 #Incrementa o tamanho da pilha

    def remover(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.prox
            self.tamanho -= 1
            return no.dado
        else:
            raise IndexError("Pilha Vazia")
        
    def observar (self):
        if self.tamanho >0:
            return self.topo.dado
        else:
            raise IndexError("Pilha vazia")
        
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while(ponteiro):
            r += str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.prox
        return r
    
    def __str__(self):
        return self.__repr__()