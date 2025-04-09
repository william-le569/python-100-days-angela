from data import resources, MENU


# process coins
# Your money is calculated here
def process_coins():
    """ Change coins into dollar"""
    print("Please insert coins.")

    number_of_quarters = float(input("How many quarters?: "))
    number_of_dimes = float(input("How many dimes?: "))
    number_of_nickles = float(input("How many nickles?: "))
    number_of_pennies = float(input("How many pennies?: "))
    
    return number_of_quarters * 0.25 + number_of_dimes * 0.1 + number_of_nickles * 0.05 + number_of_pennies * 0.01


#print report
def print_report(resources, income):
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {income}")


#customer serving
def customer_serving():
    ask = input("What would you like? (espresso/latte/cappuccino):").lower()

    return ask

# serve drinks
def serve_drinks(drink, resources, income, drink_name):
    # check whether ingredients are sufficient
    IS_SUFFICIENT = is_sufficient(drink, resources)
    if IS_SUFFICIENT:
        try:
            your_money = process_coins()
            print(f"Your money is ${round(your_money,2)}")

            IS_MONEY_SUFFICIENT, income = is_money_sufficient(your_money, drink["cost"], income, drink_name)

            if IS_MONEY_SUFFICIENT:
                make_drink(drink, resources)
                return income

        except (KeyError, ValueError) as e:
            print("You have typed in an invalid syntax. Please try again with correct one.")
    else:
        return income
  

def is_sufficient(drink, resources):
    for item in drink['ingredients']:
        if resources[item] < drink['ingredients'][item]:
            print(f"{item.title()} is not sufficient.")
            return False

    print(f"Ingredient is sufficient")

    return True

    
def is_money_sufficient(your_money, cost, income, drink_name):
    if your_money > cost:
        cash_change = your_money - cost
        income += cost

        print(f"Your cash change {round(cash_change, 2)}. Here is your {drink_name}. Thank you!")

        return True, income
    
    elif your_money == cost:
        income += cost

        print(f"It's sufficient. Here is your {drink_name}. Thank you!")

        return True, cost

    else:
        print("Your money is not sufficient")

        return False, income

def make_drink(drink, resources):
    """ This function returns remaining ingredients."""
    for item in drink['ingredients']:
        resources[item] -= drink['ingredients'][item]


def coffee_machine():
    resources_clone = {}
    resources_clone = resources
    income = 0

    while True:
        try: 
            customer_offer = customer_serving()

            if customer_offer == "report":
                print_report(resources_clone, income)
            elif customer_offer == "end":
                break
            else:
                income = serve_drinks(MENU[customer_offer], resources_clone, income, customer_offer)
        
        except (KeyError, TypeError) as e:
            print("You have typed in an invaid syntax. Please try again with correct one.")


coffee_machine()
