height = int(input("Enter your height? "))

if height > 120:
    print("You can play rollercoaster.")
    age = int(input("Enter your age? "))
    if age > 18:
        print("Your ticket costs $12.")
    elif age < 12:
        print("Your ticket costs $5.")
    else:
        print("Your ticket costs $7.")
else:
    print("You need to grow taller to play rollercoaster.")