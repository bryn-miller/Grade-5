from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, hieght=400)
canvas.pack()
canvas.create_text(150, 100, text='A pony met a pony on the way to the market,')
canvas.create_text(130, 120, text='The blue pony turned to the pink pony.',
canvas.create_text(150, 150, text='Hi there!',
font=('Times', 15))
.create_text(200, 200, text='My name is blue.',
font=('Helevtica',20))
.create_text(200, 250, text='my name is pink',
font=('Courier', 22))
.create_text(220, 300, text='and both of them went to the market place."', font=('Courier' , 30))
