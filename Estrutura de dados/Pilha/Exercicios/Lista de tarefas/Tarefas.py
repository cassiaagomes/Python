class No:
    def __init__(self, dado): 
        self.dado = dado
        self.prox = None
    
class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho
    
    def inserir (self, nova_tarefa):
        no = No(nova_tarefa)
        no.prox = self.topo
        self.topo = no
        self.tamanho += 1
    
    def remover(self):
        if self.tamanho >0:
            no = self.topo
            self.topo = self.topo.prox
            self.tamanho -= 1
            return no.dado
        else:
            raise IndexError("A Lista de tarefas está vazia")
    
    def topo (self):
        if self.tamanho > 0:
            return self.topo.dado
        else:
            raise IndexError("A lista de tarefas está vazia")
        
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while(ponteiro):
            r += str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.prox
        return r
    
    def __str__(self):
        return self.__repr__()