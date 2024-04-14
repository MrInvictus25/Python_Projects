from turtle import Turtle
ORIGINAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # The constants variable are named with all capital letters
STEP_DISTANCE = 20
# These variables are constant, they are necessary for avoiding changing a direction on opposite way, because it is prohibited
# in the official game
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self): # The code is going to determine what should happen when we initialize a new snake object.
        self.piecesSnake = []  # To organize our pieces of Snake
        self.designSnake()  # Creating a method to design a piece of snake. This method is essential to be here, because
                            # it should be executed every time I create a new object from this class
        self.head = self.piecesSnake[0]

    def designSnake(self):
        for position in ORIGINAL_POSITIONS:
            self.addPieceOfSnake(position)

    def addPieceOfSnake(self, position):
        pieceOfSnake = Turtle('square')
        pieceOfSnake.color("sandy brown")
        pieceOfSnake.penup()
        pieceOfSnake.goto(position)
        self.piecesSnake.append(pieceOfSnake)
        #print("this is piecesSnake", self.piecesSnake)
        #print("this is len", len(self.piecesSnake))

    def reset(self):
        for piece in self.piecesSnake:
            piece.goto(1000, 1000) # It allows to get rid of the previous snakes if a score is resetted
        self.piecesSnake.clear()  # All of the pieces snake that were added already to the list of piecesSnake are
                           # going to be deleted.
        self.designSnake() # Calling this method creates a new snake consisted of three pieces at the starting position
        self.head = self.piecesSnake[0]

    def expand(self):
        # Adding a new piece of snake when we reach some food
        self.addPieceOfSnake(self.piecesSnake[-1].position())  # Extraction the last element (object) from the list of the object turtles
        # position() is a method of Turtle class and it will allow to get the position of that piece of Snake.
        # Then I am going to add this new piece to the same position as the last segment.

    def movement(self):
        for pieceNumber in range(len(self.piecesSnake) - 1, 0, -1):  # It allows to overlap a path for each piece of Snake. A piece replaces
            # each other by moving on a position of previous one. (start= 2, stop= 0, step= -1) correspond the tuples of the original positions

            # We are going to set it to go to a particular X and Y position.
            # Now the X and Y position that we want it to go to is going to be the second to last piece's position.
            # The piece at position two is going to be the last piece. And then the piece at 2 - 1 is going to be the second
            # the last segment.

            nextXCord = self.piecesSnake[pieceNumber - 1].xcor()  # xcor() retrieves X coordinates
            #print("this is X cord", nextXCord)
            nextYCord = self.piecesSnake[pieceNumber - 1].ycor()  # ycor() retrieves Y coordinates
            #print("this is Y cord",nextYCord)
            self.piecesSnake[pieceNumber].goto(nextXCord, nextYCord)

        # In addition to moving these pieces, we also have to move the very first piece actually forwards by 20 paces to
        # continue moving of the snake.
        self.head.forward(STEP_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN: # it means that if the current heading is pointed down, it can't move up.
        # But for all other directions, if it's already moving up or left or right, then it can change the heading to up.
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.piecesSnake[0].setheading(RIGHT)

