import turtle as t
import random

# direction_list = ["forward", "backward", "left", "right"]

# timmy = t.Turtle()

# screen = t.Screen()

# screen.colormode(255)

# length = 15

# def walk(direction):
#     line_configuration()
#     if direction == "forward":
#         timmy.forward(length)
#     elif direction == "backward":
#         timmy.backward(length)
#     elif direction == "right":
#         timmy.right(90)
#         timmy.forward(length)
#     elif direction == "left":
#         timmy.left(90)
#         timmy.forward(length)

# def line_configuration():
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     timmy.pencolor(tup)
#     timmy.fillcolor('yellow')
#     timmy.pensize(8)
#     timmy.speed(10)

# while True:
#     random_direction = random.choice(direction_list)
#     walk(random_direction)



# screen.exitonclick()


# Solution of Angela -> make code more concise and more symmetric

# tim = t.Turtle()
# tim.color("pale green")

# colours = ["lawn green", "dark green", "medium spring green", "light sea green", "peru", "medium orchid", "magenta", "dark orange"]
# directions = [0, 90, 180, 270]

# screen = t.Screen()
# screen.colormode(255)

# def line_configuration():
#     tim.pensize(15)
#     tim.speed(10)

# while True:
#     line_configuration()
#     tim.pencolor(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# screen.exitonclick()

# Create random color
directions = [0, 90, 180, 270]

tim = t.Turtle()

screen = t.Screen()
screen.colormode(255)


def random_color_def():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def line_configuration():
    tim.pensize(15)
    tim.speed(10)

while True:
    line_configuration()
    tim.pencolor(random_color_def())
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen.exitonclick()

