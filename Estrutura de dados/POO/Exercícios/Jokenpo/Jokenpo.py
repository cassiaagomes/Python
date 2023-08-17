from Jogador import *

class Jokenpo:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
    
    def jogar(self):
        self.jogador1.realizar_escolha()
        self.jogador2.fazer_escolha()
    
    def vencedor(self):
        if self.jogador1.escolha == self.jogador2.escolha:
            print("Empate!")
        elif self.jogador1.escolha == 'PEDRA' and self.jogador2.escolha == 'TESOURA' or \
             self.jogador1.escolha == 'PAPEL' and self.jogador2.escolha == 'PEDRA' or \
             self.jogador1.escolha == 'TESOURA' and self.jogador2.escolha == 'PAPEL':
            print(f"{self.jogador1.nome} venceu!")
        else:
            print(f"{self.jogador2.nome} venceu!")