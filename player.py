from turtle import *
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.reset_player()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def reach_goal(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

