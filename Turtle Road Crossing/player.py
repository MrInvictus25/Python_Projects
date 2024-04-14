from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__() # In order to gain all abilities, the methods, and the attributes of the turtle class,
                           # we need to get this superclass to initialize itself.
        self.shape('turtle')
        self.color("sandy brown")
        self.penup()
        self.setheading(90)
        self.startPosition()  # The method that returns the turtle to the starting position

    def up(self):
        newYCoord = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), newYCoord)

    def startPosition(self):
        self.goto(STARTING_POSITION)

    def crossLine(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
