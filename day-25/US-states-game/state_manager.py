from turtle import Turtle
import pandas as pd

FONT = ("Courier", 10, "normal")
ALIGN = "CENTER"

class StateManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x = 0
        self.y = 0
        self.answer = ""

        # Read csv file
        self.state_dict = pd.read_csv("50_states.csv").to_dict()

    def print_dict(self):
        print(self.state_dict)
        print(self.answer)
        print(self.x)
        print(self.y)

    def show_result(self):
        self.goto(self.x, self.y)
        self.write(f"{self.answer}", align=ALIGN, font=FONT)

    def is_state_correct(self, answer_state):
        print(answer_state)
        for index in self.state_dict["state"]:
            print(self.state_dict["state"][index])
            if answer_state == self.state_dict["state"][index].strip().lower():
                # Retrieve data
                self.answer = self.state_dict["state"][index]
                self.x = self.state_dict["x"][index]
                self.y = self.state_dict["y"][index]
                return True
        return False
