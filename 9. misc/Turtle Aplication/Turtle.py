from tkinter import *
from math import *


class Widgets(Frame):
    def __init__(self, root):
        super(Widgets, self).__init__(root)
        self.pack()

        self.init_widgets()

    def init_widgets(self):
        self.canvas = CanvasView(self)
        self.canvas.grid(row=0)
        self.textconsole = TextConsole(self)
        self.textconsole.grid(row=1)

# ==================================== Coordination() =================================

class Coordinations:
    def __init__(self):

        self.gx = None  # global
        self.gy = None
        self.lx = None  # local
        self.ly = None
        self.originx = None
        self.originy = None

    def set_local(self, x, y):
        self.lx = x
        self.ly = y
        self.gx = self.lx + self.originx
        self.gy = - self.ly + self.originy
        return [self.gx, self.gy]


# ==================================== CanvasView =================================

class CanvasView(Canvas):
    def __init__(self, parent):
        super(CanvasView, self).__init__(parent, height=400, bg='cornsilk')
        self.config(scrollregion=self.bbox(ALL))
        #self.pack()    # canvas width -> .pack(fill=X)

        # properties
        self.width = self['width']
        self.height = self['height']
        self.center_x = int(self.width) // 2
        self.center_y = int(self.height) // 2
        self.leader_origin = (self.center_x, self.center_y)
        self.history = []
        self.leader = Leader()

        # test TODO del
        self._print(title='canvas')
        self.test()
        #

    def to_canvas_coord(self, coord):   # coord is type tuple: (x,y)
        ''' convert coordinates from local system Leader() object to global system of canvas'''
        x, y = coord
        dx, dy = self.leader_origin
        x = x + dx      # vector local x axis = [1,0]
        y = - y + dy    # vector local y axis = [0,-1]
        return (x, y)

    def draw(self):
        # if leader cleared, clear canvas and history first
        if self.leader.id == None:
            self.delete(ALL)
            self.history = []
        # add to history
        cx, cy = self.to_canvas_coord((self.leader.x, self.leader.y))
        h = (cx, cy, self.leader.pen)
        self.history.append(h)
        # draw line
        if len(self.history) > 1:
            begin = self.history[-2]
            end = self.history[-1]
            x1, y1, pen1 = begin
            x2, y2, pen2 = end
            if pen2 == 'down':
                self.create_line(x1, y1, x2, y2)
        # convert leader polygon coordinates to canvas coord. system
        cpolygon = []
        for el in self.leader.polygon:
            canvascoord = self.to_canvas_coord(el)
            cpolygon.extend(list(canvascoord))
        # draw leader
        self.__draw_leader(cpolygon)

    def __draw_leader(self, polygon):
        ''' draw leader on canvas '''
        # draw polygon
        if self.leader.id is None:
            # draw new
            self.leader.id = self.create_polygon(polygon, outline='red', fill='green', width=1)
        else:
            # change coordinates only
            self.coords(self.leader.id, polygon)

    def _print(self, title):
        print('=====', title, '=====')
        print('polygon points:', self.leader.polygon)
        print('canvas dim: ',self.width, self.height)
        print('canvas cent: ',self.center_x, self.center_y)
        print('==================')

    def test(self): # test CanvasView()
        self.draw()
        self.leader.forward(100)
        self.draw()
        self.leader.turn_left(45)
        self.draw()
        self.leader.forward(60)
        self.draw()
        self.leader.turn_left(90)
        self.draw()
        self.leader.forward(60)
        self.draw()
        self.leader.turn_right(90)
        self.draw()
        self.leader.forward(60)
        self.draw()
        self.leader.turn_right(-45)
        self.leader.pen_up()
        self.draw()
        self.leader.forward(60)
        self.draw()
        self.leader.pen_down()
        self.leader.turn_right(270)
        self.leader.forward(60)
        self.draw()
        # self.leader.clear()
        # self.draw()
        # pass

# ==================================== TextConsole =================================

# TODO dorobić sterowanie żółwiem z konsoli
class TextConsole(Text):
    def __init__(self, parent):
        super(TextConsole, self).__init__(parent)
        self.configure(height=10, width=80)
        #self.pack()
        pass

# ==================================== Leader() =================================


class Leader:
    def __init__(self):
        self.id = None  # canvas object id
        self.pen = 'down'
        self.scale = 2
        self.x = 0
        self.y = 0
        self.alpha = 0
        self.polygon_base_points = [(-1, 0), (-1, 5), (1, 5), (1, 0)]
        self.polygon = None
        self.update_polygon()

    def forward(self, dist):
        self.x = self.x + int((dist * sin(radians(self.alpha))))
        self.y = self.y + int((dist * cos(radians(self.alpha))))
        self.update_polygon()

    def turn_left(self, angle):
        self.alpha = self.alpha - angle
        self.update_polygon()

    def turn_right(self, angle):
        self.alpha = self.alpha + angle
        self.update_polygon()

    def pen_up(self):
        self.pen = 'up'

    def pen_down(self):
        self.pen = 'down'

    def clear(self):
        self.__init__()

    def update_polygon(self):
        lst = []
        for x, y in self.polygon_base_points:
            # scale
            x = x * self.scale
            y = y * self.scale
            # rotate
            coord = self.rotate(x, y, self.alpha)
            # move
            coord[0] += self.x
            coord[1] += self.y
            # add tuple to list
            lst.append((coord[0], coord[1]))
        self.polygon = lst

    def rotate(self, x, y, alpha):
            ''' calculate point coordination as rotation based on origin of coordination system;
            pivot point: x=0, y=0
            x2 = x cos(-a) - y sin(-a)
            y2 = x sin(-a) + y cos(-a)
            a<0 = means rotate left
            a>0 = means rotate right
            '''

            ar = -radians(alpha) # minus sign means alpha>0 rotate right
            x2 = x * cos(ar) - y * sin(ar)
            y2 = x * sin(ar) + y * cos(ar)
            return [int(x2),int(y2)]


# ==================================== main =================================

def main():
    root = Tk()
    root.title('Simple Language')
    app = Widgets(root)
    mainloop()


main()