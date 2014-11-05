from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)  #you were missing the end parentheses
canvas.pack()
my_image = PhotoImage(file='c:\\temp\\twilight.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)  #<-- look, you missed the _
#my_image = PhotoImage(file='C:\\Users\\Bryn Miller\\Desktop\\test.gif')
#WOOHOO!#thanks!
#you're welcome
#bye
