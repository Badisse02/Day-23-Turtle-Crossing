from turtle import *
from random import *


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.goto(300, randint(-250, 250))
            new_car.shapesize(1, 2)
            new_car.setheading(180)
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def detect_collision(self, tur):
        for car in self.cars:
            if 30 > car.xcor() > -35:
                if car.ycor() + 20 > tur.ycor() > car.ycor() - 25:
                    return False
        return True

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
