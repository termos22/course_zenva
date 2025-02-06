import turtle

t = turtle.Turtle()
scn = turtle.Screen()

for c in ["red", "green", "yellow", "blue"]:
    t.color(c)
    t.forward(75)
    t.left(90)

scn.exitonclick()
