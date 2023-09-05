import customtkinter as ctk
import phonenumbers
from phonenumbers import geocoder

window = ctk.CTk()

# Settings
window.title("Geolocation")
window.geometry("700x400")

ctk.CTkLabel(window, text="Phone Location", font=("arial bold", 20)).pack(pady=20, padx=5)
ctk.CTkLabel(window, text="What's your phone number?").pack()

def send():
    t = entry.get()
    parsed_number = parse_phone_number(t)
    location = get_location(parsed_number)
    lab.configure(text=location)

def parse_phone_number(phone_number_str):
    try:
        parsed_number = phonenumbers.parse(phone_number_str)
        return parsed_number
    except phonenumbers.phonenumberutil.NumberFormatException:
        return None

def get_location(parsed_number):
    if parsed_number:
        location = geocoder.description_for_number(parsed_number, "pt")
        return location
    else:
        return "Invalid phone number"

lab = ctk.CTkLabel(
    window,
    text="",
    width=200,
    height=25,
    text_color="#00BFFF",
    font=("arial bold", 16)
)
lab.pack(pady=10)
entry = ctk.CTkEntry(window, width=200)
entry.pack()

ctk.CTkButton(window, text="Send", width=200, command=send).pack(pady=10)

window.mainloop()

