import customtkinter as ctk
from tkinter import *
from PIL import Image

window = ctk.CTk()

window.title("Button II")
window.geometry("700x400")

ctk.CTkLabel(window, text = "Class 11 - Image", font =("arial bold", 20)).pack(pady=20, padx=5)

img = ctk.CTkImage(light_image= Image.open("./youtube.png"), dark_image= Image.open("./youtube.png"), size = (20, 20))

img1 = ctk.CTkImage(light_image= Image.open("./chatgpt.png"), dark_image= Image.open("./chatgpt.png"), size= (250,250))

ctk.CTkLabel(window, text = None,  image= img1).pack()



def evento():
    print("O botão foi clicado!")


ctk.CTkButton(window,
              text="Youtube",
              command=evento,
              image= img).pack(pady= 20)  #no state é possivel usar o "disable" para que o botão não seja mais clickavel

window.mainloop()