from turtle import *

def draw_square(size, tlo, x_cord = 0, y_cord = 0):
    penup()
    goto(x_cord, y_cord)
    pendown()
    fillcolor(tlo)
    begin_fill()
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    end_fill()

draw_square(50, "red")
draw_square(30, "blue", 100, 100)
draw_square(30, "yellow", -50, 100)
draw_square(30, "green", -50, -50)
draw_square(30, "black", 100, -50)



done()