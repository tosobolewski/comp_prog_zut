# zad 5 lista 1 pwiz

'''5. przygotować program wyświetlający tabliczkę mnożenia w wersji gracznej
      (narysowana przez nas tabela 10x10, korzystamy z canvas), korzystać z pętli.
'''

from tkinter import *


class MultiplicationTable():
    def __init__(self, _range=10, _font=8):
        self.root = None
        self.frame = None
        self.label = None
        self.canvas = None
        self._range = _range
        self._font = _font          # pixels 
        self.col_space = 3 * _font  # pixels 
        self.cv_side = self.col_space * (self._range + 2) # pixels 
        self.cv_width = self.cv_side
        self.cv_height = self.cv_side
        self.cv_bg_color = 'cornsilk'
        self.cv_label_color = 'gray'
        self.cv_product_color = 'blue'
        self.cv_color_correct = 'green'
        self.cv_color_false = 'red'
        self.cv_labels_top = []
        self.cv_labels_left = []
        self.cv_product = []
        self.question_param_current = []
        self.question_param_previous = []

        self.create_widgets()
        self.draw()
        self.create_quiz_widgets()
        self.set_color(4,7,'red')
        self.set_color(6,8,'red')
        self.root.mainloop()  # !!!
        # to poniżej już nie działa bo jest po mainloop()
        self.set_color(2,2,'red')
        print('a')
        self.root.mainloop()  # !

    def draw(self):

        cv = self.canvas
        
        for y in range(0,self._range+1):        # +1 => row/column label
            for x in range(0,self._range+1):
                px = (x+1) * self.col_space
                py = (y+1) * self.col_space

                if x==0 and y==0:
                    continue
                
                if y == 0:
                    self.cv_labels_top.append(
                        cv.create_text(px, py, text=str(x),font=(self._font),
                                       fill=self.cv_label_color)
                                       )

                elif x == 0:
                    self.cv_labels_left.append(
                        cv.create_text(px, py, text=str(y),font=(self._font),
                                       fill=self.cv_label_color)
                                       )
                    
                else:    
                    self.cv_product.append(
                        cv.create_text(px, py, text=str(x*y),font=(self._font),
                                       fill=self.cv_product_color)
                                       )

        padding = 10
        vertical_axis_offset = self.col_space * 1.5
        horizontal_axis_offset = self.col_space * 1.5
        
        x1 = padding
        y1 = vertical_axis_offset
        x2 = self.cv_width - padding
        y2 = vertical_axis_offset
        horizontal = cv.create_line(x1, y1, x2, y2)
        
        x1 = vertical_axis_offset
        y1 = padding
        x2 = vertical_axis_offset
        y2 = self.cv_height - padding
        vertical = cv.create_line(x1, y1, x2, y2)

    def create_widgets(self):
        root = Tk()
        frame = Frame(root)
        label = Label(frame, text='Multiplication Table', font=(self._font))
        canvas = Canvas(frame, bg=self.cv_bg_color,
                        width=self.cv_width, height=self.cv_height)
        root.title('Multiplication Table')
        frame.pack()
        label.pack()
        canvas.pack()
        self.root = root
        self.frame = frame
        self.label = label
        self.canvas = canvas

    def create_quiz_widgets(self):
        root = self.root
        frameq = Frame(root)
        labelq = Label(frameq, text='a * b ?')
        entryq = Entry(frameq, text='Wprowadź wynik')
        buttonq = Button(root, text='Submit')
        frameq.pack()
        labelq.pack()
        entryq.pack()
        buttonq.pack(fill=X)
        
    def set_color_lab_left(self, a, color):
        i = self.cv_labels_left[a - 1]
        self.canvas.itemconfig(i, fill=color)

    def set_color_lab_top(self, b, color):
        i = self.cv_labels_top[b - 1]
        self.canvas.itemconfig(i, fill=color)

    def set_color_product(self, a, b, color):
        i = self.cv_product[(a-1) * self._range + (b-1)]
        self.canvas.itemconfig(i, fill=color)
        
    def set_color(self, a, b, color):
        self.set_color_lab_left(a, color)
        self.set_color_lab_top(b, color)
        self.set_color_product(a, b, color)
            
    def set_default_color(self, a, b):
        self.set_color_lab_left(a, self.cv_label_color)
        self.set_color_lab_top(b, self.cv_label_color)
        self.set_color_product(a, b, self.cv_product_color)

def main():
    
    mt = MultiplicationTable(_range=10, _font=10)
    
    mt.set_color(4,7,'red')
##    n = input('wpisz coś: ')
##    mt.set_default_color(4,8)
##    mt.root.mainloop()
    pass


main()
