"""
This class is going to be able to write some text in the game that keeps track
of the score, of how many pieces of food the snake actually managed to eat.
"""

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #self.highScore = 0
        with open("data.txt") as data:
            self.highScore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)  # It is necessary to move a place for a sign before it is written
        self.hideturtle() # It allows to conceal a preliminary shape turtle
        self.updateScore()

    def updateScore(self):
        self.clear()  # It allows to clear the previous text that was written by this turtle, which is the scoreboard.
        self.write(f"Score: {self.score} High Score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def reset(self): # Resetting the scoreboard
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highScore}")
        self.score = 0
        self.updateScore()

    # def gameOver(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScore()
