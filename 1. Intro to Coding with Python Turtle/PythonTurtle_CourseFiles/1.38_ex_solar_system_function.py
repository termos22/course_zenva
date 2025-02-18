from turtle import *

speed(10)
bgcolor("black")

def draw_planet(planet_color, planet_size, distance):
    forward(distance)
    pendown()
    color(planet_color)
    begin_fill()
    circle(planet_size)
    end_fill()
    penup()


draw_planet("orange", 60, 0)
draw_planet("gray", 20, 100)
draw_planet("red", 40, 80)
draw_planet("green", 30, 90)

done()
