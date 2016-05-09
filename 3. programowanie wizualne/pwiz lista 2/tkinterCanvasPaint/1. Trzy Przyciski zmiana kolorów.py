from tkinter import *
class Drawing:
    def __init__(self, canvas, shape, storage):
        self.c = canvas
        self.s = storage
        Widget.bind(self.c, "<Button-1>", self.mouseDown)
        Widget.bind(self.c, "<Button1-Motion>", self.mouseMove)
        Widget.bind(self.c, "<ButtonRelease-1>", self.mouseUp)

        self.current_object = None
        self.shape = shape
        self.draw_function = None

        if self.shape == 'Line':
            self.draw_function = self.draw_line
        elif self.shape == 'Rectangle':
            self.draw_function = self.draw_square
        elif self.shape == 'Circle':
            self.draw_function = self.draw_circle
        else:
            pass


    def mouseDown(self, event):
        self.firstx=self.c.canvasx(event.x)
        self.firsty=self.c.canvasy(event.y)
        self.current_object = None
##        print ("values", self.firstx, self.firsty)

    def mouseMove(self, event):
        self.lastx=self.c.canvasx(event.x)
        self.lasty=self.c.canvasy(event.y)
        if self.current_object:
            self.c.delete(self.current_object)

        self.draw_function()

    def mouseUp(self, event):
        if self.s.active_button == self.s.buttons[0]:
            self.s.lines.append(self.current_object)
        elif self.s.active_button == self.s.buttons[1]:
            self.s.squares.append(self.current_object)
        elif self.s.active_button == self.s.buttons[2]:
            self.s.circles.append(self.current_object)
        else:
            pass
        print()
        print('lines:  ',self.s.lines)
        print('squares:', self.s.squares)
        print('circles:', self.s.circles)


    def draw_line(self):
        self.current_object = self.c.create_line(self.firstx, self.firsty,
                                                 self.lastx, self.lasty,
                                                 fill=self.s.active_color,
                                                 tags=self.s.buttons[0])
    def draw_square(self):
        self.current_object = self.c.create_rectangle(self.firstx, self.firsty,
                                                      self.lastx, self.lasty,
                                                      fill=self.s.active_color,
                                                      tags=self.s.buttons[1])
    def draw_circle(self):
        self.current_object = self.c.create_oval(self.firstx, self.firsty,
                                                 self.lastx, self.lasty,
                                                 fill = self.s.active_color,
                                                 tags=self.s.buttons[2])

class Storage:
    def __init__(self):
        self.colors = ['red', 'green', 'blue']
        self.buttons = ['line', 'square', 'circle']
        self.active_button = None
        self.active_color = 'black'
        self.lines = []
        self.squares = []
        self.circles = []


#--------------------------------------------------------------------------
def draw_line():
    storage.active_button = storage.buttons[0]
    Drawing(c, 'Line', storage)

def draw_rectangle():
    storage.active_button = storage.buttons[1]
    Drawing(c, 'Rectangle', storage)

def draw_circle():
    storage.active_button = storage.buttons[2]
    Drawing(c, 'Circle', storage)


def change_colorA():
    for item in c.find_withtag(storage.active_button):
        c.itemconfig(item, fill=storage.colors[0])

def change_colorB():
    for item in c.find_withtag(storage.active_button):
        c.itemconfig(item, fill=storage.colors[1])

def change_colorC():
    for item in c.find_withtag(storage.active_button):
        c.itemconfig(item, fill=storage.colors[2])
#--------------------------------------------------------------------------

# storage
storage = Storage()

colors = storage.colors

# window

okno = Tk()

# canvas
c=Canvas(okno, width=500, height=500, bg='beige')
c.pack()

# frame
ramka = Frame(okno)
ramka.pack()

# drawing buttons

b1 = Button(ramka, text='Linia', command=draw_line)
b1.grid(row=0, column=0, sticky=W+E)

b2 = Button(ramka, text='Prostokąt', command=draw_rectangle)
b2.grid(row=0, column=1, sticky=W+E)

b3 = Button(ramka, text='Koło', command=draw_circle)
b3.grid(row=0, column=2, sticky=W+E)

# color buttons

bc1 = Button(ramka, bg=colors[0], command=change_colorA)
bc1.grid(row=1, column=0, sticky=W+E)

bc2 = Button(ramka, bg=colors[1], command=change_colorB)
bc2.grid(row=1, column=1, sticky=W+E)

bc3 = Button(ramka, bg=colors[2], command=change_colorC)
bc3.grid(row=1, column=2, sticky=W+E)

# grid configuration

ramka.grid_columnconfigure(0,minsize=100)
ramka.grid_columnconfigure(1,minsize=100)
ramka.grid_columnconfigure(2,minsize=100)



okno.mainloop()
