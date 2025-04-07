import art
import random
#### simpler version of blackjack

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #13 elements

is_game_started = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def compare(u_score, c_score):
    """Compares the user score u_score against the computer score c_score."""
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def take_card(cards, player_container, player_score):
    rand_nr = random.randint(0, len(cards) - 1)
    card_value = cards[rand_nr]
    player_score += card_value
    player_container.append(card_value)
    del cards[rand_nr]

    return card_value



def black_jack():
    print("\n"*20)
    print(art.logo)
    your_cards = []
    computer_cards = []

    cards_copy = cards

    print(cards_copy)

    # global your_score
    # global computer_score
   
    your_score = 0
    computer_score = 0

    # you take 2 cards

    your_score += take_card(cards_copy, your_cards, your_score)
    your_score += take_card(cards_copy, your_cards, your_score)
 
    # computer take 2 cards

    computer_score += take_card(cards_copy, computer_cards, computer_score)
    computer_score += take_card(cards_copy, computer_cards, computer_score)

    # print(your_cards)
    print(" "*5 + f"Your cards: {your_cards}, current score: {your_score}")
    # print(computer_cards)
    print(" "*5 + f"Computer's first card: {computer_cards[0]}")

    while(your_score <= 21):
        yes_or_no = input("Type 'y' to get another card, type 'n' to pass: ")
        if yes_or_no == 'y':
            your_score += take_card(cards_copy, your_cards, your_score)
            if your_score > 21:
                did_you_go_over = True
                break
            if computer_score < 16 :
                computer_score += take_card(cards_copy, computer_cards, computer_score)
            elif computer_score >= 16 and computer_score < 21:
                computer_choice = random.randint(0, 1)
                if computer_choice == 1:
                    computer_score += take_card(cards_copy, computer_cards, computer_score)
                    if computer_score > 21:
                        does_computer_go_over = True
                        break
            # print(your_cards)
            print(" "*5 + f"Your cards: {your_cards}, current score: {your_score}")
            # print(computer_cards)
            print(" "*5 + f"Computer's first card: {computer_cards[0]}")
        elif yes_or_no == 'n': # do the judgment
            break
        
    print(" "*5 + f"Your final hand: {your_cards}, final score: {your_score}")
    print(" "*5 + f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(your_score, computer_score))

    should_continue = input("Do you want to play a game of Blackjack? Type 'y'or 'n': ")
    if should_continue == 'y':
        black_jack()
    else:
        print("Bye")
        return


if is_game_started == 'y':
    black_jack()
else:
    print("Bye!!")