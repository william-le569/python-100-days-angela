import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #13 elements

your_score = 0
player_container = []

def take_card(cards, container, your_score):
    rand_nr = random.randint(0, len(cards) - 1)
    card_value = cards[rand_nr]
    your_score += card_value
    container.append(cards[rand_nr])
    del cards[rand_nr]


take_card(cards, player_container, your_score)
print(player_container)

take_card(cards, player_container, your_score)
print(player_container)

take_card(cards, player_container, your_score)
print(player_container)

take_card(cards, player_container, your_score)
print(player_container)