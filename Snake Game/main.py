from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600) # it has a dimension of 20 pixels wide by 20 pixels tall
screen.bgcolor("black")  # Adjustment of background color
screen.title("Snake Game")  #  Setting up the title of the window that shows up.

"""
It is necessary to turn off the animation (that each separate piece of snake performs). 
The method turtle.tracer(n=None, delay=None) allows to turn turtle animation on/off and set delay for update drawings. 
If n is given, only each n-th regular screen update is really performed. It works with similarity of GIF.

The method turtle.update()performs a TurtleScreen update. To be used when tracer is turned off. 
We can tell our program when to refresh and redraw the screen.

"""
screen.tracer(0)

snake = Snake()  # Creating a new snake object from that class.
food = Food()
scoreBoard = Scoreboard()


screen.listen() # This method allows to listen buttons from keyboard
# It is necessary to change direction of the first (head) snake's piece
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


gameOver = False
while not gameOver:
    screen.update()  # Snake body will be showed up, not piece by piece, but in its entirety.
    time.sleep(0.3) # it is only going to be delayed by one second after all three segments have moved.
    snake.movement()

    # Discovering a collision between the snake and food.
    # turtle.distance(x, y=None) method returns the distance from the turtle to (x, y) the given other turtle in turtle step units.
    # x - a number or a pair/vector of numbers. y - a number if x is a number
    if snake.head.distance(food) < 15:
        food.resetCoord()
        snake.expand()
        scoreBoard.increaseScore()

    # Detect collision with a wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # gameOver = True
        # scoreBoard.gameOver()
        scoreBoard.reset()
        snake.reset()
    # Detect collision with the tail
    for piece in snake.piecesSnake[1:]:  # List of collection of the snake's pieces. # This condition is essential to avoid "Game Over" in the most beginning
        # if piece == snake.head:   # This condition is essential to avoid "Game Over" in the most beginning
        #     pass
        if snake.head.distance(piece) < 10:
            # gameOver = True
            # scoreBoard.gameOver()
            scoreBoard.reset()
            snake.reset()

screen.exitonclick()
