import random

class Jogador:
    def __init__(self, nome):
        self.nome = nome 
        self.escolha = None
    
    def realizar_escolha(self):
        pass

class jogadorHumano(Jogador):
    def realizar_escolha(self):
        while True:
          escolha = input(f"{self.nome} escolha uma das opções >> 1[PEDRA] - 2[PAPEL] - 3[TESOURA]: ")
          escolha = int(escolha)
          if escolha == 1:
              self.escolha = 'PEDRA'
              break
          elif escolha == 2:
              self.escolha = 'PAPEL'
              break
          elif escolha == 3:
              self.escolha = 'TESOURA'
              break
          else:
              print("Número inválido. Escolha uma das opções informadas.")

class jogadorNpc(Jogador):
    def fazer_escolha(self):
        for i in range(1,4):
            escolha = random.randint(1, 3)
            if escolha == 1:
                self.escolha = 'PEDRA'
                break  
            elif escolha == 2:
                self.escolha = 'PAPEL'
                break
            elif escolha == 3:
                self.escolha = 'TESOURA'
                break



        

