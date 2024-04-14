from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600) # it has a dimension of 20 pixels wide by 20 pixels tall
screen.bgcolor("black")  # Adjustment of background color
screen.title("Pong Game")
screen.tracer(0)   # The tracer() controls the animation. And in order to turn off the animation, we can put a zero in that method.


leftPaddle = Paddle((-350, 0))
rightPaddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen() # This method allows to listen buttons from keyboard
screen.onkey(key="w", fun=leftPaddle.up)
screen.onkey(key="s", fun=leftPaddle.down)
screen.onkey(key="Up", fun=rightPaddle.up)
screen.onkey(key="Down", fun=rightPaddle.down)


gameOver = False
while not gameOver:
    time.sleep(ball.moveSpeed)
    screen.update() # I have to manually update the screen and refresh it every single time.
    ball.movement()

    # Detect collision of the ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    # Detect collision with the right paddle
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 320 or ball.distance(leftPaddle) < 50 and ball.xcor() < -320:
        ball.bounceX()

    # Detect when the right Paddle exceeds the bounds
    if ball.xcor() > 380:
        ball.restartPosition()
        scoreboard.leftIncrease()
    # These statements are separate, so it is necessary to be able to calculate either right-sided player or the left-sided
    # player actually gains a point.
    # Detect when the left Paddle exceeds the bounds
    if ball.xcor() < -380:
        ball.restartPosition()
        scoreboard.rightIncrease()

screen.exitonclick()
