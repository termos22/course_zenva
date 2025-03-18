from turtle import *

diameter = 40
pop_diameter = 100

def draw_blloon():
    color("red")
    # begin_fill()
    # circle(diameter)
    # end_fill()
    dot(diameter)

def inflate_balloon():
    global diameter
    diameter = diameter + 10
    draw_blloon()

    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write("POP!")

draw_blloon()
inflate_balloon()


#onkey(inflate_balloon, "Up")
#listen()

done()
