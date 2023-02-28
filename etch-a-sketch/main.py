from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def turn_left():
    tim.setheading(tim.heading()+10)

def move_forward():
    tim.forward(20)

def move_backward():
    tim.forward(-20)

def turn_right():
    tim.setheading(tim.heading()-10)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_left, "a")
screen.onkey(move_backward, "s")
screen.onkey(turn_right, "d")

screen.exitonclick()