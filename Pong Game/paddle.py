from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__() # In order to gain all abilities, the methods, and the attributes of the turtle class,
                           # we need to get this superclass to initialize itself.
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1) # The turtle starts from 20 by 20 pixels
        self.color("sandy brown")
        self.penup()
        self.goto(position) # The left self is going to have a different coordinate from the right self.


    # I have to, again, replace paddle. with self. so that it's actually referring to the object
    # that's created from this class to get its Y coordinate or get its X coordinate.
    def up(self):
        newYCoord = self.ycor() + 20
        self.goto(self.xcor(), newYCoord)

    def down(self):
        newYCoord = self.ycor() - 20  # The X coord is not going to be alternated
        self.goto(self.xcor(), newYCoord)


