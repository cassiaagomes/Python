import customtkinter as ctk

window = ctk.CTk()

#Settings
window.title("Beta")
window.geometry("700x400")


ctk.CTkLabel(window, text = "Class 10 - (Label)", 
             font=("arial bold", 20)).pack(pady= 20, padx=5)
ctk.CTkLabel(window, text = "Another label").pack()

#Working with dinamic label
# 1: text by input
'''text_var = ctk.StringVar(value=input("Whats your name? "))
lab = ctk.CTkLabel(window,
                   textvariable =text_var,
                   width= 200, 
                   height= 25,
                   text_color="red",
                   font=("arial bold", 16))
lab.pack(pady=10)'''

#2: text by entry
def send():
    t = entry.get()
    lab.configure(text=str(t))
    pass

lab = ctk.CTkLabel(window,
                   text = "",
                   width= 200, 
                   height= 25,
                   text_color="red",
                   font=("arial bold", 16))
lab.pack(pady=10)
entry = ctk.CTkEntry(window, width=200)
entry.pack()

ctk.CTkButton(window, text= "Send", width=200, command=send).pack(pady=10)

window.mainloop() 