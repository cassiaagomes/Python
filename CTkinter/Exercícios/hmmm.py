import tkinter as tk
from tkinter import messagebox
import random

def no():
    messagebox.showinfo(' ', 'Thanks bro')
    quit()

def motionmouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

window = tk.Tk()

window.title("Beta")
window.geometry("700x400")
window.resizable(width=False, height=False)
window['bg'] = 'purple'

label = tk.Label(window, text='Are you gay?', font='Arial 20 bold', bg='white')
label.pack()

btnYes = tk.Button(window, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionmouse)

btnNo = tk.Button(window, text='Yes', font='Arial 20 bold', command=no)
btnNo.place(x=350, y=100)

window.mainloop()

