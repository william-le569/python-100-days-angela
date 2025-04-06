import art

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return round(a / b, 2)

def print_out(first_nr, next_nr, operation ,output):
    print(f"{first_nr} {operation} {next_nr} = {output} ")

operation_list = ["+", "-", "*", "\\"]
operation_dict = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
print(art.logo)

yes_or_no = 'n'
while True:    
    if yes_or_no == 'n':
        first_nr = float(input("What's the first number?: "))

    print("+\n-\n*\n\\")
    operation = input("Pick an operation: ")
    while operation not in operation_list:
        operation = input("Your entered operation is invalid. Please enter operation again: ")
    next_nr = float(input("What's the next number?: "))

    print_out(first_nr, next_nr, operation, operation_dict[operation](first_nr, next_nr))
    res = operation_dict[operation](first_nr, next_nr)

    yes_or_no = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start new calculation.")
    first_nr = res

# With the first version
# Managing operation seems to be big -> use dictionary to manage instead
