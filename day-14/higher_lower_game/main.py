import art
from game_data import data
import random
import os

# take a random item from data and ask for the first time -> this time not show your score

def higher_lower_game():
    """"Main game loop for the Higher-Lower game."""
    print(art.logo)

    # shallow copy data
    data_clone = data[:]

    # scoring
    score = 0

    current_player = take_a_player(data_clone)

    should_continue = True
    while should_continue:
        if len(data_clone) > 0:
            next_player = take_a_player(data_clone)
            result = compare_followers(current_player, next_player)

            your_guess = input("Who has more followers? Type 'A' or 'B': ").upper()

            player_list = [current_player, next_player]
            should_continue, current_player, score = score_calculation(your_guess, result, score, player_list)

        else:
            print("You are WINNER!!!!! > 0:")

            break

    yes_or_no = input("Type 'y' to continue 'n' to end the program: ")

    if yes_or_no == 'y':
        higher_lower_game()
    else:
        print("Bye. See you again!")

# take a random item representing player, make sure it is different from the first one

def take_a_player(my_list):
    """"Take a player from data-list. """
    rand_nr = random.randint(0, len(my_list)-1)
    player = my_list[rand_nr]

    del my_list[rand_nr]

    return player

# judge whether your guess is right or wrong. if right -> increase score, else -> announce it's wrong and ask to play again.

def compare_followers(current_player, next_player):
    """Compare number of followers between 2 player and return who is winner."""
    print(f"Compare A: {current_player['name']}, a {current_player['description']}, from {current_player['country']}.")
    print(art.vs)
    print(f"Compare B: {next_player['name']}, a {next_player['description']}, from {next_player['country']}.")

    if current_player['follower_count'] > next_player['follower_count']:
        return 'A'
    else:
        return 'B'

def score_calculation(your_guess, result, score, player_list):
    """Calculate score and return respectively should_continue flag, profile of current_player and score."""
    if your_guess == result:
        score += 1
        player_list[0] = player_list[1]
        should_continue = True

        os.system('cls')

        print(art.logo)
        print(f"You're right! Current score: {score}")

        return should_continue, player_list[0], score
    else:
        should_continue = False

        os.system('cls')
        
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")

        return should_continue, player_list[0], score
    

higher_lower_game()


