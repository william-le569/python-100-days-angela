import colorgram
import turtle as t
import random

# This version use Trial and Error technique to draw.

tim = t.Turtle()
tim.speed("fastest")

colors = colorgram.extract('image.jpg', 10)


screen = t.Screen()
screen.colormode(255)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)


size_of_screen = screen.screensize()
screen_width = size_of_screen[0]
screen_height = size_of_screen[1]
print(size_of_screen)


space_apart = 50
dot_size = 30

# the initial position of turtle home_x, home_y
tim.penup()
tim.hideturtle()
home_x = screen_width / 2 * (-1)
home_y = screen_height / 2 * (-1)
# tim.setpos(home_x, home_y)  # -150 , -200
tim.setpos(-195,-200)
print(tim.pos())


# tim.setpos(-400, -300)
# print(tim.pos())

def hirst_painting(num_x, num_y):
    for i in range(num_y):
        last_y = tim.pos()[1]
        last_x = tim.pos()[0]
        for j in range(num_x):
            # tim.pendown()
            tim.dot(dot_size, random_colors_def())       

            if j == num_x - 1:
                x = last_x
                y = last_y + space_apart
                # tim.penup()
                tim.setpos(x, y)
            else:
                # tim.penup()
                tim.forward(space_apart)

def random_colors_def():
    random_number = random.choice(rgb_colors)
    return random_number

hirst_painting(10, 10)

screen.exitonclick()