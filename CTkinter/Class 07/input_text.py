import customtkinter as ctk

window = ctk.CTk()

#Settings
window.title("Beta")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)

#Text box
textbox = ctk.CTkTextbox(window, width=300, height=350, scrollbar_button_color="blue", 
scrollbar_button_hover_color="white", border_color="white", border_width=3, corner_radius=15, 
fg_color="teal", border_spacing= 20)
textbox.pack()

textbox.insert("0.0", "Hello, word\n\n" + "Hi dev! I'm here programming a new graphic interface with customtkinter.\n\n"*20)

window.mainloop()