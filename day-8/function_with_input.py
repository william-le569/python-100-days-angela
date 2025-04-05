def greet():
    print("Hello!")
    print("I am from Vietnam")
    print("Can you tell me your name?")

greet()

# Function that allows input.
# Learn definitions about parameter and argument.

def greet_with_name(name):
    print("Hello, this is" + name)
    print(f"{name} comes from Vietnam")
    print(f"Can you tell {name} about yourself?")

greet_with_name("Thuan")