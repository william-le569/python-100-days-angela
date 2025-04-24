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
guessed_states = []

is_game_on = True
while is_game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?:").strip().lower()
    if answer_state == 'Exit'.lower():
        # short the code after learning list comprehension.
        missing_states = [state.title() for state in state_manager.state_dict["state"].values() if state.strip().lower() not in guessed_states]
        # missing_states = []
        # for state in state_manager.state_dict["state"].values():
        #     state = state.strip().lower()
        #     if state not in guessed_states:
        #         missing_states.append(state.title())
        print(missing_states)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        is_game_on = False
        break
 
    if state_manager.is_state_correct(answer_state):
        guessed_states.append(answer_state.strip().lower())
        state_manager.show_result()

screen.exitonclick()