from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("ivory")
        self.penup()
        self.hideturtle()  # It allows to conceal a preliminary shape turtle
        self.leftScore = 0
        #self.goto(-100, 230)
        #self.write(self.leftScore, align=ALIGNMENT, font=FONT)
        self.rightScore = 0
        #self.goto(100, 230)
        #self.write(self.rightScore, align=ALIGNMENT, font=FONT)
        self.updateScore()


    def updateScore(self):
        self.goto(-100, 230)
        self.write(self.leftScore, align=ALIGNMENT, font=FONT)
        self.goto(100, 230)
        self.write(self.rightScore, align=ALIGNMENT, font=FONT)


    def leftIncrease(self):
        self.leftScore += 1
        self.clear()
        self.updateScore()

    def rightIncrease(self):
        self.rightScore += 1
        self.clear()
        self.updateScore()
