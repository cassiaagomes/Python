import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()

janela.title("Login")
janela.geometry("500x300")

texto = ctk.CTkLabel(janela, text="Fazer Login", font =("arial bold", 20))
texto.pack(pady= 10, padx = 10)

email = ctk.CTkEntry(janela, 
                     width=200,
                     placeholder_text="Seu email... ",
                     placeholder_text_color= "grey",
                     text_color= "black",
                     font=("arial bold", 16),
                     border_color="white",
                     state = "normal")

email.pack(pady=10, padx = 10)

senha = ctk.CTkEntry(janela, 
                     width=200,
                     placeholder_text="Sua senha... ",
                     show = "•", 
                     placeholder_text_color= "grey",
                     text_color= "black",
                     font=("arial bold", 16),
                     border_color="white",
                     state = "normal")

senha.pack(pady=10, padx = 10)

check = ctk.CTkCheckBox(janela, text = "Lembrar login")
check.pack(pady= 10, padx = 10)

def clique():
    pass

botao = ctk.CTkButton(janela, text= "Login", width= 150, command=clique)
botao.pack(pady= 10, padx=10)

janela.mainloop()