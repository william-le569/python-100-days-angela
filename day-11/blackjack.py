import art

#### simpler version of blackjack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

is_game_started = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def black_jack():
    print(art.logo)

if is_game_started == 'y':
    black_jack()
else:
    print("Bye!!")