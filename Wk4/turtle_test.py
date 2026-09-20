import turtle
from operator import length_hint

t = turtle.Turtle()

def jump(t: turtle.Turtle, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def square(length, angle):
    for i in range(4):
        t.forward(length)
        t.left(angle)

t.speed(10)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
t.clear()
t.color("white")

square(50,45)
jump(t,200,100)
square(100,90)

turtle.exitonclick()