import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Crossing Game")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_cars()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if player.distance(car) < 20:
            scoreboard.display_game_over()
            game_is_on = False

    # Turtle hits the edge of the screen
    if player.ycor() >= 270:
        scoreboard.level_up()
        player.reset_position()
        carmanager.level_up()

screen.exitonclick()