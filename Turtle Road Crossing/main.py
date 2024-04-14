import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen() # This method allows to listen buttons from keyboard
screen.onkey(key="Up", fun=player.up)


gameOver = False
while not gameOver:
    time.sleep(0.1)
    # it's going to be refreshed every 0.1 seconds.
    screen.update()
    carManager.createCar() # A Car will be generated every 0.1 second when the scree refreshes
    carManager.moveCars()

    # Detect a collision with car
    for car in carManager.collectionCars:
        if car.distance(player) < 20:
           gameOver = True
           scoreboard.gameOver()

    # Detect a crossing the top bar
    if player.crossLine():    # If the turtle succeeds in crossing the line, it will be returned to
          player.startPosition()   # the starting position
          carManager.increaseSpeed()
          scoreboard.increaseLevel()

screen.exitonclick()
