# zadanie 2 lista 2 pwiz
# Wieża Hanoi



from tkinter import *

def button(column):

    if len(hanoi.hand.ring) == 0:
        if column.give(hanoi.hand):
            column.undraw(hanoi.hand.ring[0])   # TODO change list type
    else:
        hanoi.hand.give(column)
    column.draw()

    # if game is over
    if (column.name == 'C') and (len(column.rings) == 3):   # TODO change rings numbers 1 -> 3
            hanoi.hand.is_blocked = True
            hanoi.root.after(1000, hanoi.game_over) # wait 1000 ms
            #print('game over!')


def buttonA():
    button(hanoi.columns[0])

def buttonB():
    button(hanoi.columns[1])

def buttonC():
    button(hanoi.columns[2])

    
class WieżaHanoi:
    def __init__(self, scale=2, rings=3): # TODO scale

        self.root = None # root window tkinter

        self.columns = []
        self.rings = []
        self.buttons = []
        self.hand = Hand()
        
        self.canvas = None
        self.canvas_width = 300 * scale
        self.canvas_height = 100 * scale
        

        self.margin = 10       
        
        # root window
        self.root = Tk()
        self.root.title('Wieża Hanoi')
        
        # frame main
        frame = Frame(self.root)
        frame.pack()
        
        # canvas
        self.canvas = Canvas(frame, bg='cornsilk',
                             width=self.canvas_width, height=self.canvas_height)
        self.canvas.grid(row=0, columnspan=3)

        # buttons
        button_col=0
        for t in ['A','B','C']:
            b = Button(frame, text=t)
            b.grid(column=button_col, row=1)
            self.buttons.append(b)
            button_col += 1
            
        foo = [buttonA, buttonB, buttonC]
        for i in range(3):
            self.buttons[i].config(command=foo[i])

        # columns create
        names = ['A', 'B', 'C']
        col_dist = 100
        level_zero = 90 
        for n in [-1,0,1]:
            r1 = Rect((self.canvas_width/2) + (n * col_dist), level_zero, 100, 20 ) # Rect(x, y, b, h)
            r2 = Rect((self.canvas_width/2) + (n * col_dist), level_zero, 10, 80 ) # Rect(x, y, b, h)
            c = Column(self.canvas, geometry=[r1, r2], name=names[n+1]) # name = 'A' | 'B' | 'C'
            self.columns.append(c)

        # rings create
        for width, color in [(30, 'red'), (20,'green'), (10, 'yellow')]:
            ring = Ring(width, color)
            self.columns[0].add(ring)
        # draw first column with all three rings
        self.columns[0].draw()

    def game_over(self):
        from time import time, sleep
        sleep(2)
        self.canvas.delete(ALL)
        self.canvas.create_text(150,35, text='YOU WIN!',
                                 font = ('arial', 25),
                                 fill = 'blue')


class Rect:                     # class calculate rectangle coordinates
    def __init__(self, x, y, b, h):
        self.x = x
        self.y = y
        self.b = b
        self.h = h
        self.x1 = x - b/2
        self.x2 = x + b/2
        self.y1 = y
        self.y2 = y - h


class Ring:
    def __init__(self, width, color_):
        self.width = width
        self.color = color_
        self.canvas_ID = None


class Column:
    def __init__(self, canvas, geometry, name):
        self.name = name
        self.rings = []
        self.canvas = canvas
        self.geometry = geometry

        # draw columns
        for gm in geometry:
            self.canvas.create_rectangle(gm.x1, gm.y1, gm.x2, gm.y2, fill='black')

    def add(self, ring):
        if len(self.rings) == 0:
            self.rings.append(ring)
            return True
        elif ring.width < self.rings[-1].width:    # ascending order of size, smallest ring on top
            self.rings.append(ring)
            return True
        else:
            return None

    def give(self, obj):
        if len(self.rings) > 0:
            el = self.rings.pop()
            if obj.add(el):
                return True
            else:
                self.rings.append(el)
                return False

    def draw(self):
        axis_y = 90 - 20
        axis_x = self.geometry[0].x
        level = 0
        for ring in self.rings:
            if ring.canvas_ID:
                level += 17 # space between rings
                continue
            geom = Rect(axis_x, axis_y - level, ring.width, 15) # Rect(x, y, b, h)
            ring.canvas_ID = self.canvas.create_rectangle(geom.x1, geom.y1,
                                                          geom.x2, geom.y2,
                                                          fill = ring.color)
            level += 17
            #print('---ring.canvas.ID: ', ring.canvas_ID, 'color', ring.color)
        #print('column draw: ', len(self.rings))

    def undraw(self, ring):
        self.canvas.delete(ring.canvas_ID)
        #print('undraw ring.canvas_ID: ', ring.canvas_ID, 'color', ring.color )
        ring.canvas_ID = None


class Hand:
    def __init__(self):
        self.ring = []  # TODO change list type
        self.is_blocked = False
        pass

    def add(self, ring):
        if self.is_blocked:
            return False
        if len(self.ring) == 0:
            self.ring.append(ring)
            if len(self.ring) == 1:
                return True
            else:
                return False
        else:
            return False

    def give(self, obj):
        if len(self.ring) == 1:
            el = self.ring.pop()
            if obj.add(el):
                return True
            else:
                self.ring.append(el)
                return False


#====================================== main ====================================

hanoi = WieżaHanoi(scale=1, rings=3)
mainloop()
