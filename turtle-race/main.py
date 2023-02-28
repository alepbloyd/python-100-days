from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtle_dict = {}

start_x = -230
start_y = -100


for color in colors:
  turtle_dict[color] = Turtle(shape="turtle")
  turtle = turtle_dict[color]
  turtle.penup()
  turtle.color(color)
  turtle.goto(x=start_x,y=start_y)
  start_y += 30

is_race_on = False

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in turtle_dict:
    if turtle_dict[turtle].xcor() > 230:
      is_race_on = False
      winning_color = turtle_dict[turtle].pencolor()
      if winning_color == user_bet:
        print(f'You\'ve won! The {winning_color} turtle is the winner!')
      else:
        print(f'You\'ve lost! The {winning_color} turtle won.')
    random_distance = random.randint(1,10)
    turtle_dict[turtle].forward(random_distance)


screen.exitonclick()