from turtle import *
from random import *

bgcolor("medium slate blue")
hideturtle()
speed(0)
width = window_width()
height = window_height()

def losowy_kolor():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return (red / 255.0, green / 255.0, blue / 255.0)


def draw_star(xpos, ypos):
    size = randrange(4, 10)
    penup()
    goto(xpos, ypos)
    pendown()
    kolor = losowy_kolor()
    dot(size, kolor)

def draw_moon():
    size = randrange(40, 100)
    xpos = randrange(round( -width / 2), round(width / 2))
    ypos = randrange(round(-height / 2), round(height / 2))
    penup()
    goto(xpos, ypos)
    pendown()
    kolor = losowy_kolor()
    dot(size, kolor)


draw_moon()


for i in range(500):
    xpos = randrange(round( -width / 2), round(width / 2))
    ypos = randrange(round(-height / 2), round(height / 2))
    draw_star(xpos, ypos)



done()