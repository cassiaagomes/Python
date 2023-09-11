import re
n = 3
email = [None]*n

for i in range(n):
    try:
        email[i] = input("Digite seu e-mail: ")
        if re.search("com$", email[i]) and re.search("@", email[i]):
            print("O e-mail {} possui '@' e termina com '.com'".format(email[i]))
        else:
            print("O e-mail {} não possui '@' nem termina com '.com'".format(email[i]))
    except Exception as e:
        print(f"Erro: {e} ")








