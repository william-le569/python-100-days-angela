import turtle

screen = turtle.Screen()

# Set custom coordinate system
# screen.setworldcoordinates(-150, -200, 150, 200)
# screen.setworldcoordinates(-1000, -1000, 1000, 1000)

screen.setup(800, 600)

screen = turtle.Screen()
screen.bgcolor("lightblue") 

# screen.screensize(800, 600)

# Create a turtle and move to the home position (0, 0)
t = turtle.Turtle()
t.setpos(-380, -280)  # Home position in new coordinates

print(f"window size: {screen.window_width()} {screen.window_height()}")
print(screen.screensize())
canvas = turtle.getcanvas()
print("canvas pixel size =", canvas.winfo_width(), "x", canvas.winfo_height())


screen.exitonclick()