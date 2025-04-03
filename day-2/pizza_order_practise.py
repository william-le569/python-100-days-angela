print("Welcome to Python Pizza Deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra chese? Y or N: ")

total_cost = 0

if size == 'S':
    total_cost += 15
    if pepperoni == 'Y':
        total_cost += 2
elif size == 'M':
    total_cost += 20
    if pepperoni == 'Y':
        total_cost += 3
else:
    total_cost += 25
    if pepperoni == 'Y':
        total_cost += 3

if extra_cheese == 'Y':
    total_cost += 1

print(f"Your final bill is: ${total_cost}")