from turtle import Turtle, Screen

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


screen.exitonclick()