import turtle

def mysquare(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
        

t = turtle
t = turtle.Pen()
t.reset()
t.begin_fill()
mysquare(50, True)
t.end_fill()

