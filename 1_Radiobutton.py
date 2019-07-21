import tkinter as tk
from tkinter import ttk

window = tk.Tk()

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def Cal():
    redSal = redVar.get()
    if redSal == 1: window.configure(background=COLOR1)
    elif redSal == 2: window.configure(background=COLOR2)
    elif redSal == 3: window.configure(background=COLOR3)


redVar = tk.IntVar()

rad1 = tk.Radiobutton(window, text="Rad1" , variable=redVar, value=1, command=Cal)
rad1.grid(column=0 , row=0)

rad2 = tk.Radiobutton(window, text="Rad2" , variable=redVar, value=2, command=Cal)
rad2.grid(column=0 , row=1)

rad3 = tk.Radiobutton(window, text="Rad3" , variable=redVar, value=3, command=Cal)
rad3.grid(column=0 , row=2)

window.mainloop()
