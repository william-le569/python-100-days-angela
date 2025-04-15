import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.setworldcoordinates(-1000, -1000, 1000, 1000)

print("screensize (canvas units):", screen.screensize())

canvas = turtle.getcanvas()
print("canvas (pixels):", canvas.winfo_width(), "x", canvas.winfo_height())


print("window width (pixels):", screen.window_width(), "window height: ", screen.window_height())
screen.exitonclick()