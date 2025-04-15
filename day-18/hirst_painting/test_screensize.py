import turtle

screen = turtle.Screen()

# Set custom coordinate system
# screen.setworldcoordinates(-150, -200, 150, 200)
# screen.setworldcoordinates(-1000, -1000, 1000, 1000)

screen.screensize(1000, 1000)

# Create a turtle and move to the home position (0, 0)
t = turtle.Turtle()
t.setpos(0, 0)  # Home position in new coordinates

print(screen.screensize())

screen.exitonclick()