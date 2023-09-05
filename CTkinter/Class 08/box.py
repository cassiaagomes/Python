import customtkinter as ctk

window = ctk.CTk()

#Settings
window.title("Beta")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width=500, height=300)
window.resizable(width=False, height=False)

#Box
def open():
    dialogbox = ctk.CTkInputDialog(title = "Dialog box", text = "What's your phone number?", 
    entry_border_color="teal", entry_fg_color="white")
    print(dialogbox.get_input())


btn = ctk.CTkButton(window, text="Open the box", command=open)
btn.pack()

window.mainloop()