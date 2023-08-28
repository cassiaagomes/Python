import customtkinter as ctk

window = ctk.CTk()

#Settings
window.title("Beta")
window.geometry("700x400")
window.maxsize(width=900, height=500)
window.minsize(width=500, height= 300)
window.resizable(width=False, height=False)

#Theme
window._set_appearance_mode("system")

#New size
def new_screen():
    new_window = ctk.CTkToplevel(window) #create a new window 
    new_window.title("secondary screen")
    new_window.geometry("200x200")

btn_newscreen = ctk.CTkButton(master= window, text="Open new window", command= new_screen).place(x=280, y=100)

window.mainloop()