import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
  def __init__(self):
    self.car_list = []
    self.move_increment = MOVE_INCREMENT

  def create_car(self, move_increment):
    new_car = Car(color=random.choice(COLORS), start_y=random.randint(-250,250), move_increment=move_increment)
    self.car_list.append(new_car)

  def move_cars(self):
    for car in self.car_list:
      car.move_left()