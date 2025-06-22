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

money = 0

def report():
    print(f"Water : {resources['water']}mL")
    print(f"Milk : {resources['milk']}mL")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money:.2f}")


def coin_calculation():
    print("Please insert coins")

    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many penniess?: "))
    cost = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return cost

def coffee_process(drink,cost):
    global money
    ingredients = MENU[drink]["ingredients"]
    drink_cost = MENU[drink]["cost"]
    print(f"Here is ${cost-drink_cost:.2f} in change.")
    print(f"Here is your {drink} ☕️. Enjoy!")
    for item in ingredients:
        resources[item] -= ingredients[item]
    money += drink_cost

def is_resource_sufficient(ingredients):
    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            return False
    return True

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        report()
    elif is_resource_sufficient(MENU[choice]["ingredients"]):
        total_cost = coin_calculation()
        drink_cost = MENU[choice]["cost"]
        if total_cost < drink_cost:
            print("Sorry, that's not enough money. Money refunded.")
        else:
            coffee_process(choice, total_cost)
    else:
        print(f"Not sufficient ingredients to make {choice}.Please Order another drink")
