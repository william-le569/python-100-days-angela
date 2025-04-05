
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
draw_message = "You draw!"
win_message = "You win!"
lose_message = "You lose!"

invalid_message = "Invalid choice!"

list = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

if your_choice <  3 and your_choice >= 0:
    print(list[your_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(list[computer_choice])

if your_choice >= 3 or your_choice < 0:
    print(invalid_message)
elif your_choice == 2 and computer_choice == 0:
    print(lose_message)
elif your_choice == 0 and computer_choice == 2:
    print(win_message)
elif your_choice > computer_choice:
    print(win_message)
elif your_choice < computer_choice:
    print(lose_message)
elif your_choice == computer_choice:
    print(draw_message)
  

