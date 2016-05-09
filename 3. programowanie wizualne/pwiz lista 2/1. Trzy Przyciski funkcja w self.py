from tkinter import *
class Drawing:
    def __init__(self, canvas, shape):
        self.c = canvas
        Widget.bind(self.c, "<Button-1>", self.mouseDown)
        Widget.bind(self.c, "<Button1-Motion>", self.mouseMove)
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


    def draw_line(self):
        self.current_object = self.c.create_line(self.firstx, self.firsty,\
                                                 self.lastx, self.lasty)
    def draw_square(self):
        self.current_object = self.c.create_rectangle(self.firstx, self.firsty,\
                                                 self.lastx, self.lasty,
                                                      fill='blue')

    def draw_circle(self):
        self.current_object = self.c.create_oval(self.firstx, self.firsty,\
                                             self.lastx, self.lasty,
                                                     fill = 'gray')

#--------------------------------------------------------------------------
def draw_line():
    Drawing(c, 'Line')

def draw_rectangle():
    Drawing(c, 'Rectangle')        

def draw_circle():
    Drawing(c, 'Circle')

#--------------------------------------------------------------------------    
okno = Tk()

b1 = Button(okno, text='Linia', command=draw_line)
b1.pack(side=LEFT)

b1 = Button(okno, text='Prostokąt', command=draw_rectangle)
b1.pack(side=LEFT)

b1 = Button(okno, text='Koło', command=draw_circle)
b1.pack(side=LEFT)

c=Canvas(okno, width=500, height=500, bg='beige')
#c.create_rectangle(10, 10, 100, 100, fill='brown')
c.pack()
#Drawing(c, 'Rectangle')
okno.mainloop()
