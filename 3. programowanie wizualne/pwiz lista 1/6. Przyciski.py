# zad 5 lista 1

'''6. Przygotować program z 4 (można też 8) małymi przyciskami do sterowania
      i polem tekstowym (Label), na razie wyswietlać w polu tekstowym, który
      przycisk został wciśnięty.
'''
import tkinter as tk

class GameDirectionButtons:
    def __init__ (self, root_frame):
        self.root_frame = root_frame
        self.root_frame_parent = root_frame.nametowidget(root_frame.winfo_parent())
        self.label = []
        self.buttons = []
        self.but_num = 4
        self.but_pos = [[0,1],[1,2],[2,1],[1,0]]
        self.but_commands = [self.up, self.right, self.down, self.left]
        self.create_label()
        self.create_buttons()
        self.deploy_buttons()
        
    def up(self):
        self.label.config(text='up')

    def right(self):
        self.label.config(text='right')

    def down(self):
        self.label.config(text='down')

    def left(self):
        self.label.config(text='left')

    def create_label(self):
        self.label = tk.Label(self.root_frame_parent,
                              text='direction',
                              anchor=tk.CENTER,
                              relief=tk.RIDGE,
                              pady=10)
        self.label.pack(fill=tk.X)
   
    def create_buttons(self):
        for i in range(self.but_num):
            self.buttons.append(tk.Button(self.root_frame,
                                          text='B-'+str(i)))
        
    def deploy_buttons(self):
        i = 0
        for button in self.buttons:
            button.grid(row=self.but_pos[i][0], column=self.but_pos[i][1])
            button.config(command=self.but_commands[i])
            i += 1

def main():

    win = tk.Tk()
    root_frame = tk.Frame()

    gdb = GameDirectionButtons(root_frame)

    root_frame.pack()
        

main()
