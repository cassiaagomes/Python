class Visor:
    def __init__(self, dado):
        self.dado = dado
    
    def set_dado(self, dado):
        self.dado = dado
    
    def get_dado(self):
        return self.dado
    
    def zerar(self):
        self.set_dado(0.0)


class BombaCombustivel:
    GASOLINA = "gasolina"
    ALCOOL = "alcool"

    def __init__(self, tipo_combustivel, preco_litro):
        self.tipo_combustivel = tipo_combustivel
        self.preco_litro = preco_litro
        self.visor_total_a_pagar = Visor(0.0)
        self.visor_litros = Visor(0.0)
        self.visor_preco_litro = Visor(self.preco_litro)

    def set_preco_litro(self, preco_litro):
        self.preco_litro = preco_litro
    
    def zerar(self):
        self.visor_total_a_pagar.zerar()
        self.visor_litros.zerar()

    def abastecer(self, valor_maximo):
        self.zerar()
        litros = valor_maximo / self.preco_litro

        for i in range(int(round(litros, 2))):
            self.visor_litros(i)
            self.visor_total_a_pagar(round(i * self.preco_litro, 2))
            

        self.visor_litros.set_dado(litros)
        self.visor_total_a_pagar.set_dado(valor_maximo)

class BombaPostGasolina:

    def __init__(self):
        self.bomba_gasolina = BombaCombustivel(BombaCombustivel.GASOLINA, valor = 5.89)
        self.bomba_alcool = BombaCombustivel(BombaCombustivel.ALCOOL, valor = 2.45)
    
    def abastecer_gasolina(self, valor_maximo):
        self.bomba_gasolina.abastecer(valor_maximo)

    def abastecer_alcool(self, valor_maximo):
        self.bomba_alcool.abastecer(valor_maximo)

    def alterar_preco_gasolina(self, novo_valor):
        self.bomba_gasolina.set_preco_litro(novo_valor)
    
    def alterar_preco_alcool(self, novo_valor):
        self.bomba_alcool.set_preco_litro(novo_valor)
    
    def zerar_bomba_gasolina(self):
        self.bomba_gasolina.zerar()
    
    def zerar_bomba_alcool(self):
        self.bomba_alcool.zerar()