import customtkinter as ctk

window = ctk.CTk()

window.title("Button II")
window.geometry("700x400")

ctk.CTkLabel(window, text = "Class 15 - Segmented button", font =("arial bold", 20)).pack(pady=20, padx=5)

def botao(value):
    print("Voce está em:", value)

segment = ctk.CTkSegmentedButton(window, 
                                 values = ["Tkinter", "Django", "Flask"],
                                 command = botao,
                                 text_color= "black",
                                 fg_color = "teal",
                                 selected_color="red",
                                 selected_hover_color= 'green',
                                 border_width=5,
                                 width= 10,
                                 corner_radius= 30,
                                 unselected_color="blue",
                                 unselected_hover_color="white")

segment.pack(pady= 20)
segment.set("Django")

window.mainloop()