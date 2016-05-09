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

        self.create_widgets()
        self.draw()

    def draw(self):

        cv = self.canvas
        
        for y in range(0,self._range+1):
            for x in range(0,self._range+1):
                px = (x+1) * self.col_space
                py = (y+1) * self.col_space

                if x==0 and y==0:
                    continue
                
                if y == 0:
                    cv.create_text(px, py, text=str(x),
                                   font=(self._font), fill='gray')
                elif x == 0:
                    cv.create_text(px, py, text=str(y),
                                   font=(self._font), fill='gray')
                else:    
                    self.canvas.create_text(px, py, text=str(x*y),
                                            font=(self._font), fill='blue')


    def create_widgets(self):
        root = Tk()
        frame = Frame(root)
        label = Label(frame, text='Multiplication Table', font=(self._font))
        canvas = Canvas(frame, bg='cornsilk', width=self.cv_width, height=self.cv_height)
        root.title('Multiplication Table')
        frame.pack()
        label.pack()
        canvas.pack()
        self.root = root
        self.frame = frame
        self.label = label
        self.canvas = canvas

def main():
    
    mt = MultiplicationTable(_range=10, _font=10)
    
    
    pass


main()
