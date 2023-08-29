import customtkinter as ctk

window = ctk.CTk()

#Settings
window.title("Beta")
window.geometry("700x400")
window.maxsize(width=900, height=550)
window.minsize(width= 500, height= 300)
window.resizable(width=False, height= False)

#Frames
frame1 = ctk.CTkFrame(master = window, width= 200, height= 330, fg_color= "teal", bg_color= "transparent", border_width= 10, corner_radius=30).place(x = 10, y = 60)
frame2 = ctk.CTkFrame(master = window, width= 200, height= 330, fg_color= "pink", bg_color="transparent", border_width= 10, corner_radius=30).place(x = 230, y = 60)
frame3 = ctk.CTkFrame(master = window, width= 200, height= 330, fg_color= "white", bg_color="transparent", border_width= 10, corner_radius=30).place(x = 450, y = 60)

window.mainloop()