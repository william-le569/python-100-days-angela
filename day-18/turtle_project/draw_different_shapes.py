import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
screen.colormode(255)

length = 100

# procedural programming

# for i in range(3,11):
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     print(tup)
#     timmy.pencolor(tup)
#     for j in range(i):
#         timmy.forward(length)
#         timmy.right(-360/i)

# for i in range(3,11):
#     tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     print(tup)
#     timmy.pencolor(tup)
#     for j in range(i):
#         timmy.forward(length)
#         timmy.left(360/i)

# procedural programming -> use function

def draw_shape(num_sides, direction):
    tup = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    timmy.pencolor(tup)
    angle = 360/num_sides
    if direction == "left":
        angle *= -1
    elif direction == "right":
        pass
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

# draw_shape(3, "left")

for num_sides in range(3, 11):
    draw_shape(num_sides, "right")
for num_sides in range(3, 11):
    draw_shape(num_sides, "left")
screen.exitonclick()