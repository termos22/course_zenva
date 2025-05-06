from turtle import *

def draw_line():
    forward(10)
    penup()
    forward(5)
    pendown()
    dot(5)
    penup()
    forward(5)
    pendown()

for i in range(15):
    draw_line()

done()
