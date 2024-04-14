# from turtle import Turtle, Screen
import turtle as turtle
from random import choice, randint

almondTurtle = turtle.Turtle()
turtle.colormode(255)

def randomColor():
    # RGB representation
    color = ()
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = color + (r,) + (g,) + (b,)
    return color


almondTurtle.speed("fastest")

def drawSpirograph(sizeOfGap): # The variable "sizaOfGap" is a size that is going to be in between each
                            # of these circles that are being drawn.

    for circle in range(360 // sizeOfGap): # It draws a circle shifting 5 degrees each time
        almondTurtle.color(randomColor())
        almondTurtle.circle(100) # Radius
        # currentHeading = almondTurtle.heading() # Access to a method to alternate the turtle's state
        almondTurtle.setheading(almondTurtle.heading() + sizeOfGap) # Setting  the orientation of the turtle to a specific angel. 0 - East, 90 - North, 180 - West, 270 - South



drawSpirograph(5)

screen = turtle.Screen() # To be capable of keeping a screen for an essential time
screen.exitonclick()

