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
    
    def inserir(self, novo_dado):
        no = No(novo_dado)
        no.prox = self.topo
        self.topo = no
        self.tamanho += 1

    def remover(self):
        if self.tamanho > 0:
            no = self.topo
            self.topo = self.topo.prox
            self.tamanho -= 1
            return no.dado
        else:
            raise IndexError("Pilha vazia")
        
    def observar(self):
        if self.tamanho > 0:
            return self.topo.dado
        else:
            raise IndexError("Pilha vazia")
    
    def __len__(self):
        return self.tamanho
    
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while(ponteiro):
            r += str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.prox
        return r
    
    def __str__(self):
        return self.__repr__()
    


pilha = Pilha()
pilha.inserir(3)
pilha.inserir(7)
pilha.inserir(25)
pilha.inserir(38)
pilha.inserir(16)
print(pilha)
pilha.remover()
print(pilha)