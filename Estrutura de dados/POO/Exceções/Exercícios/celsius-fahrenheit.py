class Temperatura:
    def __init__(self):
        self._temperatura = 0
    
    @property
    def temperatura(self):
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, nova_temperatura):
        self._temperatura = nova_temperatura
    
    def atualizar_temperatura(self):
        try:
            atual = float(input("Digite a temperatura atual em Celsius: "))
            t_fahrenheit = ((atual * 9) + 160) / 5
            self._temperatura = t_fahrenheit
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar um número válido.")
    
    def __str__(self) -> str:
        return f"A temperatura em Fahrenheit é: {self._temperatura}"


temp = Temperatura()
temp.atualizar_temperatura()
print(temp)





    


