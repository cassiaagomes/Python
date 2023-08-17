import calendar

class Calendario:
    def __init__(self):
        self.ano = int(input("Ano: "))
        self.mes = int(input("Mês: "))
    
    def exibir_mes(self):
        cal = calendar.month(self.ano, self.mes)
        print(cal)

calendario = Calendario()
calendario.exibir_mes()
