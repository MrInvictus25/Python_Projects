"""
 The food class is going to know how to render itself as a small circle on the screen. And then every time the snake touches
 the food, then that food is going to move to a new random location.
"""
from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle") # This is a method that the turtle class has that I am now going to modify in my food class.
        self.penup()   # When I initialize a new piece of food, I want to be convinced that it has a circular shape,
                   # and I am also going to pen up it so that it is not drawn.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.resetCoord()

    def resetCoord(self):
        randomXcord = random.randint(-280, 280)
        randomYcord = random.randint(-280, 280)
        self.goto(randomXcord, randomYcord)
