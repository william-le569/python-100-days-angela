import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.speed("fastest")

current_angle = 0
step = 5
radius = 100

def random_color_def():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_circle(radius, angle):
    tim.setheading(angle)
    tim.circle(radius)
   

def line_configuration():
    tim.pensize(1)

while current_angle < 360:
    tim.pencolor(random_color_def())
    line_configuration()
    draw_circle(radius, current_angle)
    print(tim.heading())
    current_angle += step



screen.exitonclick()