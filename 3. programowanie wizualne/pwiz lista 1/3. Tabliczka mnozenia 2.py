# zad 3 lista 1 pwiz

'''3. przygotować program wyświetlający tabliczkę mnożenia w wersji tekstowej
      (grid 10x10), korzystać z pętli.
'''


import tkinter as tk

win = tk.Tk()

for y in range(1,21):
    for x in range(1,21):

        # nagłówki
        if y == 1:
            lista = tk.Label(win, text=str(x),font='Helvetica 12', bg='gray')\
                        .grid(row=0,column=x)
        
        if x == 1:
            lista = tk.Label(win, text=str(y),font='Helvetica 12', bg='gray')\
                        .grid(row=y,column=0)

        # wartości w tabeli
        lista = tk.Label(win, text=str(x*y),font='Helvetica 12')\
                .grid(row=y,column=x)

