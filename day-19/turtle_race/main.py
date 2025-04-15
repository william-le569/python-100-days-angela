import turtle as t
import random

screen = t.Screen()
window_with = 500
window_height = 400
screen.setup(width=window_with, height=window_height)

def turtle_race():
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    # print(user_bet)
    is_race_on = False
    turtle_list = []

    x_coordinate = (-1)*window_with / 2 + 50
    y_coordinate = (-1)*window_height / 2 + 30
    for index in range(6):
        new_turtle = t.Turtle(shape="turtle")
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.color(colors[index])
    
        new_turtle.goto(x_coordinate, y_coordinate)
        y_coordinate += 50

        turtle_list.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    choice = screen.textinput(f"You've won! The {winning_color} turtle is the winner!", "Enter color of play to start the race again or 'exit' to out:")
                    if choice == "exit":
                        is_race_on = False
                    else:
                        is_race_on = True
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                    choice = screen.textinput(f"You've lost! The {winning_color} turtle is the winner!", "Enter 'yes' to start the race again or 'no' to out:").lower()
                    if choice == "no":
                        print("See you again!")
                        is_race_on = False
                        break
                        
                    elif choice == "yes":
                        screen.clear()
                        turtle_race()
                        
            turtle.speed("fastest")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

turtle_race()

screen.exitonclick()