import customtkinter as ctk
from tkinter import *

window = ctk.CTk()

#Settings
window.title("Button")
window.geometry("700x400")

ctk.CTkLabel(window, text = "Class 11 - Entry", font =("arial bold", 20)).pack(pady=20, padx=5)

entry = ctk.CTkEntry(window, 
                     width=300,
                     placeholder_text="What's your name? ",
                     placeholder_text_color= "white",
                     fg_color= "#A020F0",
                     text_color= "white",
                     font=("arial bold", 16),
                     border_color="#8A2BE2",
                     state = "normal",
                     corner_radius=20)
entry.pack(pady=20)

def catch():
    print(entry.get())
    entry.delete(0, END)

'''def delet():
    entry.delete(0, END)
    ctk.CTkButton(window, width=300, text="Delet text", command=delet).pack(pady=5)
    '''

ctk.CTkButton(window, width=300, text="Catch text", command=catch).pack()


window.mainloop()