import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_nr_of_chars = nr_letters + nr_symbols + nr_numbers

# Hard version:

password = ""

count_letters = 0
count_symbols = 0
count_numbers = 0

for i in range(0, total_nr_of_chars):
    random_choice = random.randint(0, 2)
    if random_choice == 0:
        if count_letters < nr_letters:
            count_letters += 1
            password += random.choice(letters)
        elif count_symbols < nr_symbols:
            count_symbols += 1
            password += random.choice(symbols)
        elif count_numbers < nr_numbers:
            count_numbers += 1
            password += random.choice(numbers)
    elif random_choice == 1:
        if count_symbols < nr_symbols:
            count_symbols += 1
            password += random.choice(symbols)
        elif count_letters < nr_letters:
            count_letters += 1
            password += random.choice(letters)
        elif count_numbers < nr_numbers:
            count_numbers += 1
            password += random.choice(numbers)
    elif random_choice == 2:
        if count_numbers < nr_numbers:
            count_numbers += 1
            password += random.choice(numbers)
        elif count_letters < nr_letters:
            count_letters += 1
            password += random.choice(letters)
        elif count_symbols < nr_symbols:
            count_symbols += 1
            password += random.choice(symbols)

print(password)


######### Comments on code #######

# Areas for Improvement:
# Complexity: The logic with multiple if-elif chains and counters makes the code harder to read and maintain.
# There’s a simpler way to achieve the same result.
# Redundancy: The nested conditions repeat similar checks (e.g., count_letters < nr_letters)
#  across different branches, which could be streamlined.
# Edge Cases: If the random choices don’t align well, the code might prioritize one type of character
# over others unintentionally, though your counters mitigate this somewhat.
# Style: The code could benefit from better formatting and more concise approaches 
# (e.g., using lists and shuffling instead of manual character-by-character construction).
