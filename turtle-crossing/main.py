from turtle import Screen
import time
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")
move_increment = 10

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()

  if random.randint(1,10) > 8:
    car_manager.create_car(move_increment=move_increment)

  car_manager.move_cars()

  for car in car_manager.car_list:
    if car.distance(player) < 20:
      scoreboard.game_over()
      game_is_on = False

  if player.is_at_finish_line():
    move_increment += 10
    scoreboard.update_level()
    player.go_to_start()


screen.exitonclick()