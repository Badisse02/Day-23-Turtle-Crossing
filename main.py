import time
from player import *
from car_manager import *
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

car = CarManager()

scoreboard = Scoreboard()
scoreboard.print_score()

screen.listen()

screen.onkey(key="Up", fun=player.go_up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    if car.detect_collision(player):
        car.car_move()
    else:
        game_is_on = False
        scoreboard.game_over()
    if player.reach_goal():
        player.reset_player()
        scoreboard.score += 1
        scoreboard.print_score()
        car.level_up()

screen.exitonclick()
