from calculadora import *


def main():
  operacao = Calculadora()

  while True:
    operacao.interface()
    opcao = input("Escolha uma operação: ")

    if opcao == '+':
      print('Operação: +')
      operacao.somar()
    elif opcao == '-':
      print('Operação: -')
      operacao.subtrair()
    elif opcao == '*':
      print('Operação: *')
      operacao.multiplicar()
    elif opcao == '/':
      print('Operação: /')
      operacao.dividir()
    elif opcao == 'r':
      print('Operação: RESETAR')
      operacao.resetar()
    else:
      print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
  main()

