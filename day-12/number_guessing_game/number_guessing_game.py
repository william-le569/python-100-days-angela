import art
import random

should_continue = True

while should_continue:
    print(art.logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty_level == "easy":
        attempts = 10
    elif difficulty_level == "hard":
        attempts = 5

    hidden_number = random.randint(1, 100)

    do_guess_again = True

    while do_guess_again:
        if attempts > 0:
            if attempts == 1:
                print(f"You have {attempts} attempt remaining to guess the number.")
            else:
                print(f"You have {attempts} attempts remaining to guess the number.")
            guessing_number = int(input("Make a guess:   "))
            if guessing_number > hidden_number:
                attempts -= 1
                print("Too high")
                do_guess_again = True
            elif guessing_number < hidden_number:
                attempts -= 1
                print("Too low")
                do_guess_again = True
            else:
                print(f"You are correct. The number is {hidden_number}")
                do_guess_again = False
        else:
            print(f"You are out of attempts. The correct number is {hidden_number}")
            do_guess_again = False
    
    yes_or_no = input("Do you want to continue yes or no? 'y' or 'no': ")
    if yes_or_no == 'y':
        should_continue = True
        print(20*"\n")
    elif yes_or_no == 'no':
        should_continue = False

