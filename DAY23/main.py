import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
player = Player()
screen.listen()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move_forward,"Up")
screen.onkey(player.move_backward,"Down")
screen.onkey(player.turn_left,"Left")
screen.onkey(player.turn_right,"Right")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()

    car_manager.create_car()

    car_manager.move_car()
    if player.ycor() == 280:
        scoreboard.level += 1
        scoreboard.create_scoreboard()
        player.create_player()
        car_manager.car_speed *= 0.7

    for car in car_manager.all_car:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on = False



screen.exitonclick()
