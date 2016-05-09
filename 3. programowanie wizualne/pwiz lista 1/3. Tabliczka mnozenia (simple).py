# zad 3 lista 1 pwiz

import tkinter as tk

win = tk.Tk()

for y in range(1,11):
    for x in range(1,11):
 
        lista = tk.Label(win, text=str(x*y),font='Helvetica 12')\
                .grid(row=y,column=x)
        




