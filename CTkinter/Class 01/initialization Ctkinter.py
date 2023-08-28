import customtkinter as ctk

window = ctk.CTk() #Create our window

window._set_appearance_mode("light") # ----> this line let our window in light theme

btn = ctk.CTkButton(window, text = 'Oi!')
btn.pack()


window.mainloop() #Initialization

