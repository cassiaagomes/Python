class Conversor:
    def __init__(self):
        self._valor = 0

    
    def real_para_dolar(self):
        real = float(input("Digite o valor em reais para converter: "))
        try:
            if real > 0:
                converter = real / 4.98
                self._valor = round(converter)
        except ValueError:
             print('Valor inválido.')
    
    def dolar_para_real(self):
        dolar = float(input("Digite o valor em dolar para converter: "))
        try:
            if dolar > 0:
                converterdol = dolar * 4.98
                self._valor = round(converterdol)
        except ValueError:
             print('Valor inválido.')

    
    def __str__(self):
        return f"Você terá aproximadamente: {self._valor}"

val = Conversor()
val.dolar_para_real()
print(val)
