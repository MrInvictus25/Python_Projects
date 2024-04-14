from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self): # Here, it is necessary to create all of our cars.
        self.collectionCars = []  # So I'm going to create a list called collectionCars
        self.carSpeed = STARTING_MOVE_DISTANCE

    def createCar(self): # This method will be executed in main.py file to generate a random car somewhere along
                          # the Y-axis with a provided dimension.
        frequency = random.randint(1, 6)
        if frequency == 1:   # this basically ensures that every six times the while loop runs a new car will
                             # be generated.
            newCar = Turtle()
            newCar.shape('square')
            newCar.shapesize(stretch_wid=1, stretch_len=2)  # The turtle starts from 20 by 20 pixels
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomYCord = random.randint(-250, 250)
            newCar.goto(300, randomYCord)
            self.collectionCars.append(newCar)

    def moveCars(self):
        for car in self.collectionCars:
            car.backward(self.carSpeed)

    def increaseSpeed(self):
        self.carSpeed += MOVE_INCREMENT

