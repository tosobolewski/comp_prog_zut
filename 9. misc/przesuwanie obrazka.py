from tkinter import *

root = Tk()

canvas = Canvas(root, bg='cornsilk',
                width=300, height=300)
canvas.pack()


photo = []
canvas.pieces_id = []

file_path =  'king' + '.gif'
photo = PhotoImage(file=file_path)

x = 100
y = 100

id = canvas.create_image(x, y,image=photo)
#print(id)
canvas.pieces_id.append(id)


canvas.coords(id, 200,200)  # dobre !

# canvas.itemconfig(id, x=150, y=150)


root.mainloop()
