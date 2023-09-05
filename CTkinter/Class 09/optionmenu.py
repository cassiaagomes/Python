import customtkinter as ctk

window = ctk.CTk()

#settings
window.title("Beta")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)

ctk.CTkLabel(window, text= "Options", font=('arial bold', 20)).pack(pady=20, padx=5)

ctk.CTkLabel(window, text= "Choose your birth month", font=("arial bold", 14)).pack()

month_var = ctk.StringVar(value = "Choose you birth month")

def birth_month(choose):
    print(f"Your birth month is: {choose} ")


mes = ctk.CTkOptionMenu(window, 
                  values = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 
                            "Setembro", "Outubro", "Novembro", "Dezembro"],
                            command=birth_month,
                            variable=month_var,
                            width = 250,
                            height= 25,
                            corner_radius= 50,
                            fg_color="teal",
                            button_color="white",
                            button_hover_color="blue",
                            dropdown_fg_color="red",
                            dropdown_text_color="white",
                            dropdown_font=("arial bold", 15))



mes.pack(pady=10)


'''mes = ctk.CTkOptionMenu(window, 
                  values = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", 
                            "Setembro", "Outubro", "Novembro", "Dezembro"],
                            command=birth_month)


mes.pack(pady=10)
mes.set("Month...")'''



window.mainloop()