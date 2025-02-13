from turtle import *

speed(0)

Screen().bgcolor("black")

#create orange planet
color("orange")
begin_fill()
circle(60)
end_fill()
penup()

# create grey planet
forward(100)
color("gray")
pendown()
begin_fill()
circle(20)
end_fill()
penup()

# create red planet
forward(80)
color("red")
pendown()
begin_fill()
circle(40)
end_fill()
penup()

# create green planet
forward(90)
color("green")
pendown()
begin_fill()
circle(30)
end_fill()


done()
