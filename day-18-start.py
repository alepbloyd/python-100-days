import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

colors = ['red','green','blue']

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
    # draw_shape(shape_side_n)

def random_turn():
    angle_options = [0,90,180,270]
    return random.choice(angle_options)

def random_walk(walk_length):
    tim.pensize(10)
    tim.speed(10)
    for x in range(walk_length):
        tim.setheading(random_turn())
        tim.color(random_rgb())
        tim.forward(20)

def random_rgb():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)

# random_walk(1000)

def circle_spiro():
    tim.speed("fastest")
    for _ in range(1,100):
        tim.color(random_rgb())
        tim.circle(100)
        tim.right(5)

circle_spiro()



screen = t.Screen()
screen.exitonclick()