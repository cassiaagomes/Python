from Jogador import *
from Jokenpo import *

print('::::::::> JOKENPO <::::::::')

nome_jogador = input("Digite o seu nome: ")
jogador_humano = jogadorHumano(nome_jogador)
jogador_npc = jogadorNpc("Computador")

jogo = Jokenpo(jogador_humano, jogador_npc)

jogo.jogar()
print(f"{jogador_humano.nome} escolheu: {jogador_humano.escolha}")
print(f"Computador escolheu: {jogador_npc.escolha}")

jogo.vencedor()

