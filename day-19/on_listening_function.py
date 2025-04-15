import turtle as t


tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

screen.listen()
# screen.onclick("Right", move_forward)
screen.onkey(key="Right", fun=move_forward)

screen.exitonclick()