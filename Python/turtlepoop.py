import turtle
size = 1
sides = 100
slobby_dog=70
e = turtle.Pen()
# s = turtle.banana
for s in range(0, sides):
     e.left(360/sides)
     #e.forward(30)
     e.right(size)
     e.forward(20)
     size = size + 5
