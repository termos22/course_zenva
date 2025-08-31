from turtle import *
move_distance  = 20
bgcolor("#D2691E")
speed(0)
width = window_width()
height = window_height()

penup()
goto((width /2) - 200, height / 2)
pendown()

color("blue")
begin_fill()
goto(width /2, height / 2)
goto(width /2, - (height / 2))
goto((width /2) - 200, - (height / 2))
goto((width /2) - 200, height / 2)
end_fill()

penup()
goto(-200, 0)
shape("turtle")
color("green")

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()
    check_borders()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()
    check_borders()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()
    check_borders()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()
    check_borders()

def check_goal():
    if xcor() > (width /2) - 200:
        color("pink")
        hideturtle()
        color("white")
        write("YOU WIN!")
        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")

def check_borders():
    if xcor() < - (width / 2):
        goto (0, 0)

    if ycor() > (height / 2):
        goto(0, 0)

    if ycor() < - (height / 2):
        goto(0, 0)





onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()


done()