import turtle

t = turtle.Turtle()
scn = turtle.Screen()
turtle.bgcolor("#000000")

for c in ["red", "green", "yellow", "blue", "pink", "cyan"]:
    t.color(c)
    t.forward(90)
    t.left(60)

scn.exitonclick()
