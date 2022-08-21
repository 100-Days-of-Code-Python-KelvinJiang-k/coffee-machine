MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_resources(coffee_type, resources, MENU):
    ingredients_required = MENU[coffee_type]["ingredients"]
    for ingredient in ingredients_required:
        if ingredients_required[ingredient] > resources[ingredient]:
            return False
    return True


def alter_resources(coffee_type, resources, MENU):
    ingredients_required = MENU[coffee_type]["ingredients"]
    for ingredient in ingredients_required:
        resources[ingredient] -= ingredients_required[ingredient]
    return True


def enough_money(coffee_type, money, MENU):
    coffee_cost = MENU[coffee_type]["cost"]
    if coffee_cost > money:
        return False
    return True


def calculate_change(coffee_type, money, MENU):
    cost = MENU[coffee_type]["cost"]
    return money - cost


def coffee_machine(resources, MENU):
    machine_working = True
    while machine_working:
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        while not (coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino" or coffee_type == "off"):
            print("Invalidate input, please try again.")
            coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

        if coffee_type == "off":
            machine_working = False
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            money = 0.25 * quarters + 0.10 * dimes + 0.5 * nickels + 0.01 * pennies

            if enough_money(coffee_type, money, MENU) and enough_resources(coffee_type, resources, MENU):
                change = calculate_change(coffee_type, money, MENU)
                alter_resources(coffee_type, resources, MENU)
                print(f"Here is ${change} in change.")
                print(f"Here is your {coffee_type}, enjoy.")
            elif not enough_money(coffee_type, money, MENU):
                print("You do not have enough money.")
            elif not enough_resources(coffee_type, resources, MENU):
                print("We do not have enough resources.")
                machine_working = False

coffee_machine(resources, MENU)


