
import turtle as turtle
from random import choice, randint
almondTurtle = turtle.Turtle()
almondTurtle.speed("fastest")
turtle.colormode(255)
almondTurtle.penup() # Getting rid of lines
almondTurtle.hideturtle()

colorList = [(246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

almondTurtle.setheading(225)  # 225 degrees
almondTurtle.forward(300)  # Distance
almondTurtle.setheading(0)

amountOfDots = 100

for dot in range(1, amountOfDots + 1):
    almondTurtle.dot(20, choice(colorList))   # Drawing a circular dot with diameter size, using color. If size is not given, the maximum of pensize+4 and 2*pensize is used.
    almondTurtle.forward(50)

    if dot % 10 == 0:
        almondTurtle.setheading(90)
        almondTurtle.forward(50)  # Distance
        almondTurtle.setheading(180)
        almondTurtle.forward(500) # Going forward by 10 times 50 places
        almondTurtle.setheading(0) #  Turning around a turtle





screen =  turtle.Screen() # To be capable of keeping a screen for an essential time
screen.exitonclick()
