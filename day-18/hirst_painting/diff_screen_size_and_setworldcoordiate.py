# import turtle
# screen = turtle.Screen()
# screen.setworldcoordinates(-150, -200, 150, 200)
# t = turtle.Turtle()
# t.setpos(0, 0)
# print(screen.screensize())  # Outputs pixel size, e.g., (400, 300)
# screen.exitonclick()


### GPT

import turtle

screen = turtle.Screen()

# Set up the window to a specific size in pixels
screen.setup(width=800, height=600)

# Set the logical coordinate system to something unusual
# This means 1 canvas unit ≠ 1 pixel
screen.setworldcoordinates(-1000, -1000, 1000, 1000)

# Get the screen size in canvas units (not pixels)
print("screensize() =", screen.screensize())

# Get the actual canvas (drawable area) size in pixels
canvas = turtle.getcanvas()
print("canvas pixel size =", canvas.winfo_width(), "x", canvas.winfo_height())

# Get the full window size (including title bar etc.)
root = canvas.winfo_toplevel()
print("window pixel size =", root.winfo_width(), "x", root.winfo_height())

turtle.done()