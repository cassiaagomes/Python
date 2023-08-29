import customtkinter as ctk

window = ctk.CTk()

window.title("Beta")
window.geometry("700x400")
window.maxsize(width= 900, height= 550)
window.minsize(width= 500, height= 300)
window.resizable(width=False, height=False)

#TabView
tabview = ctk.CTkTabview(master= window, width= 400, corner_radius=20, border_width=3, border_color= "white", 
fg_color= "teal", segmented_button_fg_color= "white", segmented_button_selected_color= "green", segmented_button_unselected_hover_color= "black")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idade")
tabview.add("Genero")
tabview.tab("Nomes").grid_columnconfigure(0, weight=1)
tabview.tab("Idade").grid_columnconfigure(0, weight=1)
tabview.tab("Genero").grid_columnconfigure(0, weight=1)


# Add new elements
text = ctk.CTkLabel(tabview.tab("Nomes"), text=" Cássia Gomes\n Lavinia Albuquerque\n Gael Braga")
text.pack()
idd = ctk.CTkLabel(tabview.tab("Idade"), text=" 22\n 4\n 2")
idd.pack()
gen = ctk.CTkLabel(tabview.tab("Genero"), text=" F\n F\n M")
gen.pack()



window.mainloop()