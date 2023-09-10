import customtkinter as ctk

window = ctk.CTk()

window.title("Button II")
window.geometry("700x400")

ctk.CTkLabel(window, text = "Class 14 - slider", font =("arial bold", 20)).pack(pady=20, padx=5)

def slider_value(value):
    if value == 10:
        slider.configure(fg_color="#BA55D3")
    else: 
        slider.configure(fg_color = "#A020F0")
    print(round(value))

slider = ctk.CTkSlider(window, 
                       from_= 0, to = 100, 
                       command = slider_value,
                       width=500,
                       button_color="white",
                       button_hover_color="#1E90FF",
                       button_length=10,
                       corner_radius= 10,
                       fg_color="white",
                       progress_color="#00BFFF")
slider.pack(pady=30)

window.mainloop()