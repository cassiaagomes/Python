'''try: #Bloco try para executar as tentativas e verificar a possibilidade de execução
  num1 = int(input('Digite um número:')) 
except ValueError: #Except para valores invalidos na tentativa do primeiro numero
    print('Erro na digitação do primeiro número')
else:    # caso não caia no try, entra no else para uma nova informação
  try: #Bloco try para a tentativa do numero 2
    num2 = int(input('Digite outro número:'))
  except ValueError: #Except para valores invalidos na tentativa do primeiro numero
    print('Erro na digitação do segundo número')
  else: #caso não haja erro...
    try:  # é realizado uma tentativa de divisão divisão 
      div = num1 / num2
    except ZeroDivisionError: # Caso de uma divisão por zero ---> Erro
      print('Erro Divisão por zero!!')   
    else:    
      print(f'Divisão = {div}')  
finally:
      print("FIM!!")'''


#Outra solução ----------------------------------------------------------------------
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

try:
    div = num1/num2
except ValueError:
    print("Divisão invalida. Digite outro número.")
except ZeroDivisionError:
    print("Não é possivel dividir por zero. Tente novamente.")
else:
    print(f"O resultado da divisão é: {div}")
finally:
    print("Fim!")
