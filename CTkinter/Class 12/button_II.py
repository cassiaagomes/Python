import customtkinter as ctk
from tkinter import *
from PIL import Image

window = ctk.CTk()

window.title("Button II")
window.geometry("700x400")

ctk.CTkLabel(window, text = "Class 11 - Button", font =("arial bold", 20)).pack(pady=20, padx=5)

img = ctk.CTkImage(light_image=Image.open("./youtube.png"), dark_image=Image.open("./youtube.png"),
                   size= (20, 20))

def evento():
    print("O botão foi clicado!")


ctk.CTkButton(window,
              text="Youtube",
              command=evento,
              width=300,
              height=20,
              fg_color="transparent",
              hover_color="green",
              text_color="red",
              font=("arial bold", 18),
              border_color="white",
              border_width=3,
              border_spacing=2,
              corner_radius=20,
              state="normal",
              image= img).pack(pady= 20)  #no state é possivel usar o "disable" para que o botão não seja mais clickavel

window.mainloop()