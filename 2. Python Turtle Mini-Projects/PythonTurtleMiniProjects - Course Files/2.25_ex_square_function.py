from turtle import *

def draw_square(size, x_cord = 0, y_cord = 0):
    penup()
    goto(x_cord, y_cord)
    pendown()
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)

draw_square(50)
draw_square(30, 100, 100)
draw_square(30, -50, 100)
draw_square(30, -50, -50)
draw_square(30, 100, -50)



done()