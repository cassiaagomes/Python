import os


class Calculadora:
    def __init__(self):
        self._valor_total = 0 #Deve começar com 0 pois o valor a ser exibido é ZERO!!!
    
    @property
    def valor(self):
        return self._valor_total
    
    @valor.setter
    def valor(self, valor):
        if valor != 'x':
            self._valor_total = valor
        else:
            raise ValueError("Voce deve inserir um novo valor")
    
    def interface(self):
        print(f'+--------------------+\n')
        print(f'|             {self._valor_total}|\n')
        print(f'+--------------------+\n')
        print('(+) Somar')
        print('(-) Subtrair')
        print('(*) Multiplicar')
        print('(/) Dividir')
        print('(r) Resetar\n')
        print('------------------------')
    
    def limpar_terminal(self):
        sistema_operacional = os.name
        if sistema_operacional == 'posix':
            os.system('clear')
        elif sistema_operacional == 'nt': 
            os.system('cls')
    
    def somar(self):
        print('DIGITE X A QUALQUER M0MENTO PARA MUDAR A OPERAÇÃO\n')
        while True:
            novo_valor = input('Valor: ')
            if novo_valor.lower() == 'x':
                break 
            try:
                if self._valor_total == 0:
                    valor_numerico = float(novo_valor)
                    self._valor_total = valor_numerico
                    break
                else:
                    valor_numerico = float(novo_valor)
                    self._valor_total += valor_numerico
                    self.limpar_terminal()
                    self.interface()
            except ValueError:
                print('Valor inválido. Insira um número válido.')
    
    def multiplicar(self):
        print('DIGITE X A QUALQUER M0MENTO PARA MUDAR A OPERAÇÃO\n')
        while True:
            novo_valor = input('Valor: ')
            if novo_valor.lower() == 'x':
                break
            try:
                if self._valor_total == 0:
                    valor_numerico = float(novo_valor)
                    self._valor_total = valor_numerico
                    break
                else:
                    valor_numerico = float(novo_valor)
                    self._valor_total *= valor_numerico
                    self.limpar_terminal()
                    self.interface()
            except ValueError:
                print('Valor inválido. Insira um número.')

    def subtrair(self):
        print('DIGITE X A QUALQUER M0MENTO PARA MUDAR A OPERAÇÃO\n')
        while True:
            novo_valor = input('Valor: ')
            if novo_valor.lower() == 'x':
                break
            try:
                if self._valor_total == 0:
                    valor_numerico = float(novo_valor)
                    self._valor_total = valor_numerico
                    break
                else:
                    valor_numerico = float(novo_valor)
                    self._valor_total -= valor_numerico
                    self.limpar_terminal()
                    self.interface()
            except ValueError:
                print('Valor inválido. Insira um número válido')
    
    def dividir(self):
        print('DIGITE X A QUALQUER M0MENTO PARA MUDAR A OPERAÇÃO\n')
        while True:
            novo_valor = input('Valor: ')
            if novo_valor.lower() == 'x':
                break
            try:
                if self._valor_total == 0:
                    valor_numerico = float(novo_valor)
                    self._valor_total = valor_numerico
                    break
                else:
                    valor_numerico = float(novo_valor)
                    self._valor_total /= valor_numerico
                    self.limpar_terminal()
                    self.interface()
            except ValueError:
                print('Valor inválido. Insira um número.')
    
    def resetar(self):
        self._valor_total = 0
        self.limpar_terminal()
        self.interface()
    
            
    
    

            
    
