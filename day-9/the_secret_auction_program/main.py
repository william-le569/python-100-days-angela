from os import system
import art

print(art.logo)

##################

print("Welcome to the secret auction program.")

auction = {}

should_continue = True
max = 0
while should_continue:
    name = input("What is your name?:")
    bid = int(input("What is your bid?: $"))

    auction[name] = bid
    if bid > max:
        max = bid
        max_name = name

    has_other_bidders = input("Are there other bidders? 'yes' or 'no'.").lower()

    if has_other_bidders == 'no':
        should_continue = False

print(f"The winner is {max_name} with a bid of ${max}")




