class Idade:
    def __init__(self):
        self.__idade = 0
    
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade_atual):
        self.__idade = idade_atual
    
    def conferir_idade(self):
        try: 
            idade = int(input("Informe a sua idade atual: "))
            if idade >= 18:
                print("Você atingiu a maior idade.")
                self.__idade = idade
            else:
                print("Você ainda não atingiu a maior idade. ")
        except ValueError:
            print("Apenas números. Tente novamente. ")
        
    def __str__(self):
        return f"A sua idade atual é de: {self.__idade}"
    

age = Idade()
age.conferir_idade()
print(age)