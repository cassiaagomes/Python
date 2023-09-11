'''try:
    senha = (input("Digite sua senha: "))
    if len(senha) == 8:
        print("O tamanho desta senha é adequado.")
    else:
        print("Senha inválida.")
except ValueError:
    print("Apenas números. Digite outra senha")
finally:
    print("Fim!")'''

import getpass

class Senha:
    def __init__(self):
        self.__senha = 0 
    
    @property
    def senha (self):
        return self.__senha
    
    @senha.setter
    def senha (self, nova_senha):
        self.__senha = nova_senha
    
    def atualizar_senha(self):
        try:
            senha = getpass.getpass("Digite sua senha: ")
            if len(senha) == 8:
                print("O tamanho desta senha é adequado.")
                self.__senha = senha
            else:
                print("Senha inválida.")
        except ValueError:
            print("Apenas números. Digite outra senha")
    
    def __str__(self) -> str:
        return f"A sua senha atual é: {self.__senha}"
    


senh = Senha()
senh.atualizar_senha()
print(senh)