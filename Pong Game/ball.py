from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("ivory")
        self.shape("circle")
        self.penup()
        self.xMove = 10  # When the ball hits the wall it should reverse a direction. So if it was increasing,
        self.yMove = 10 # it needs to decrease. If it was decreasing, it needs to increase by amount of steps
        self.moveSpeed = 0.1

    def movement(self):
        newXCord = self.xcor() + self.xMove
        newYCord = self.ycor() + self.yMove
        self.goto(newXCord, newYCord)


    def bounceY(self):
        self.yMove *= -1  # When a bounce occurs however it is essential to change a yMove.
        # So that it's the opposite in terms of direction of what it used to be.
        # So if it used to be +10 we want it to be now -10, and if it used to be -10, it should be now +10.

    def bounceX(self):
        self.xMove *= -1
        self.moveSpeed *= 0.9  # It allows to reduce a figure, then a sleep method decreases

    def restartPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1  # Resetting the speed to an original value if one of the paddles misses the ball
        self.bounceX()  # To get the ball to reverse its X-axis.
