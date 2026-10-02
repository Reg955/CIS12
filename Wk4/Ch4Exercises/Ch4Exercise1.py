import turtle

t=turtle.Turtle()

def rectangle(w, h):
    t.up(h)
    t.goto(w,h)
    t.down()

"""This function prompts a user to enter the radius of a circle as an integer and 
uses the math module to calculate the area and circumference.  It prints the area and 
circumference in a f-string"""

