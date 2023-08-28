import customtkinter as ctk

window = ctk.CTk()

#Settings
window.title("Beta")
window.geometry("700x400")
window.maxsize(width=900, height=500)
window.minsize(width=500, height= 250)
window.resizable(width=False, height=False)

#Custom theme
window._set_appearance_mode("light") #Light/Dark/System theme

window.mainloop()