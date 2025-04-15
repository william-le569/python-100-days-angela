import turtle

# Set up window and canvas
screen = turtle.Screen()
screen.setup(width=800, height=600)  # Window size in pixels

# Align canvas units with pixel units
# Logical coordinates from (0, 0) to (800, 600)
screen.setworldcoordinates(0, 0, 800, 600)

# Create turtle and go to bottom-left
t = turtle.Turtle()
t.penup()
t.goto(0, 0)  # Bottom-left corner in this coordinate system
t.dot(10, "red")  # Optional: draw a dot so you can see it

screen.exitonclick()