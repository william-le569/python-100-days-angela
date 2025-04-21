import turtle
import pandas as pd
from state_manager import StateManager

screen = turtle.Screen()

screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

# Create an anonymous object.
turtle.Turtle()
turtle.shape(image)
state_manager = StateManager()

# This function to retrieve x, y of a location on click
#-----------------------------------------------------
# def get_mouse_click_coor(x, y):
#     # turtle.onscreenclick(None)
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# # other method to keep our screen open
# turtle.mainloop()
#------------------------------------------------------


is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?:").strip().lower()
    if answer_state == 'no':
        is_game_on = False
        break
 
    if state_manager.is_state_correct(answer_state):
        state_manager.show_result()

screen.exitonclick()