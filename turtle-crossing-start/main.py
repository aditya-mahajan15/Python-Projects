import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_manager.hideturtle()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.move_up)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect Collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect successfull crossing
    if player.at_finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.inc_level()

screen.exitonclick()
