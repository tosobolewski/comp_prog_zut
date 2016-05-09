# zad 4 lista 1 pwiz

''' 4. Przećwiczyć umieszczanie przycisków za pomocą metod pack i grid.
        a) Utworzyć listę przycisków (w pętli, ok. 20 przycisków),
        b) umieścić przyciski przy pomocy metody pack (wykorzystać parametry
        poznane na wykładzie),
        c) umieścić przyciski przy pomocy metody grid (np. umieścić przyciski na
        obwodzie prostok¡ta, w kształcie diamentu),
        d) zaimplementować funkcję, która przyjmuje 3 parametry: obiekt zawie-
        raj¡cy przyciski (okno Tk lub Frame), sposób rozmieszczenia i listę
        przycisków, wywołać tą funkcję 3 razy dla różnych ramek (Frame).
        '''

import tkinter as tk

# ===================== create button list =========================

def create_buttons(widget, number=20):
    button_list = []
    for i in range(number):
        button_list.append(tk.Button(widget, text='B-'+str(i), bg='red', fg='white'))
    return button_list

# ===================== buttons in pack() =========================

def buttons_pack(buttons):
    ''' deploy buttons in pack() form'''

    for b in buttons:
        b.pack(fill=tk.BOTH)

    print(buttons[0].pack_info())
    parent = buttons[0].pack_info()
    print(parent['in'].pack_slaves())
    #print(win_pack.pack_slaves())


# ================ buttons in square on grid() ======================

def buttons_square(buttons):
    print('a')
    n = len(buttons)
    side= n // 4
    LT = [0, 0]
    RT = [0, side]
    RB = [side, side]
    LB = [side, 0]
    e = 0
    if side > 2:
        for i in range(side):
            buttons[i].grid(row=LT[0], column=LT[1]+i, sticky=tk.W+tk.E)
            buttons[i+side].grid(row=RT[0]+i, column=RT[1], sticky=tk.W+tk.E)
            buttons[i+2*side].grid(row=RB[0], column=RB[1]-i, sticky=tk.W+tk.E)
            buttons[i+3*side].grid(row=LB[0]-i, column=LB[1], sticky=tk.W+tk.E)


# =============== buttons in diamond on grid() ======================

def buttons_diamond(buttons=[]):
    n = len(buttons)
    side= n // 4
    L = [side-1, 1]     # Left
    T = [1, side+1]     # Top
    R = [side+1, 2*side-1]  # Right
    B = [2*side-1, side-1]  # Bottom
    e = 0
    if side > 2:
        for i in range(side):
            buttons[i].grid(row=L[0]-i, column=L[1]+i, sticky=tk.W+tk.E)
            buttons[i+side].grid(row=T[0]+i, column=T[1]+i, sticky=tk.W+tk.E)
            buttons[i+2*side].grid(row=R[0]+i, column=R[1]-i, sticky=tk.W+tk.E)
            buttons[i+3*side].grid(row=B[0]-i, column=B[1]-i, sticky=tk.W+tk.E)

# =============== deploy buttons in window/frame ======================

def deploy_buttons(widget=None, form='none', buttons=None):
    if widget is None:
        widget = tk.Tk()    # new window
        widget.title(form)  # new name           

    if buttons is None:
        buttons = create_buttons(widget)
            
    if form == 'pack':
        buttons_pack(buttons)
    elif form == 'square':
        buttons_square(buttons)
    elif form == 'diamond':
        buttons_diamond(buttons)
    else:
        pass
    
# ============================= main ===================================

def main():

##    deploy_buttons(widget=None, form='pack', buttons=None)
##    deploy_buttons(widget=None, form='square', buttons=None)
##    deploy_buttons(widget=None, form='diamond', buttons=None)


##    win_pack = tk.Tk()
##    win_pack.title('My pack()')
##    buttons = create_buttons(win_pack, 20)
##    deploy_buttons(win_pack, 'pack', buttons)
##    lab = tk.Label(win_pack, text='Labelka')
##    lab.pack()
##
##    win_grid_sq = tk.Tk()
##    win_grid_sq.title('My square')
##    buttons = create_buttons(win_grid_sq, 60)
##    deploy_buttons(win_grid_sq, 'square', buttons)
##
##    win_grid_diam = tk.Tk()
##    win_grid_diam.title('My diamond')
##    buttons = create_buttons(win_grid_diam, 60)
##    deploy_buttons(win_grid_diam, 'diamond', buttons)


    win = tk.Tk()
    f1 = tk.Frame(win)
    f1.pack(side=tk.RIGHT)

    f2 = tk.Frame(win)
    f2.pack()

    f3 = tk.Frame(win)
    f3.pack(side=tk.LEFT)

    deploy_buttons(f1, form='pack', buttons=None)
    deploy_buttons(f2, form='square', buttons=None)
    deploy_buttons(f3, form='diamond', buttons=None)


main()
    
