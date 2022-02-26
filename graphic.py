from turtle import *

speed(0)
pensize(2)
penup()
pencolor('indigo')
bgcolor('black')
setup(800,800)
goto(10,0)
pendown()

for i in range(75):
    right(-97)
    forward(i*6)

hideturtle()
exitonclick()
