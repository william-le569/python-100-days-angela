import turtle as t

screen = t.Screen()
tim = t.Turtle()

screen.listen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_cw():
    # step = 10
    # global angle
    # angle += step
    # tim.setheading(angle)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def rotate_ccw():
    # step = 10
    # step = step * (-1)
    # global angle
    # angle += step
    # tim.setheading(angle)   
    new_heading = tim.heading() - 10 
    tim.setheading(new_heading)

def clear_screen():
    tim.home()
    tim.clear()

screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = rotate_cw)
screen.onkey(key = "d", fun = rotate_ccw)
screen.onkey(key = "c", fun = clear_screen)
screen.exitonclick()