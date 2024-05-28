from art import logo
from art import thanks

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 25,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 45,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(logo)
def is_resource_sufficient(order_ingredients):
    #this is for enough resource
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_rupees():
    print("Insert rupees of 100 / 200 / 500 only.")
    amount = int(input("Enter rupees ₹"))
    if amount == 100:
        print(f"Received ₹{amount}")
    elif amount == 200:
        print(f"Received ₹{amount}")
    elif amount == 500:
        print(f"Received ₹{amount}")
    else:
        print("Invalid Input. Try later")
    return amount


def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or False if money is insufficient and refunded"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ₹{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money is refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")
    print(thanks)

is_on = True

while is_on:
    print("Hey Welcome, A lot can happen over coffee!")
    print("Coffee crafted with Care. \n"
          "Espresso: ₹25 \n"
          "Latte: ₹45 \n"
          "Cappuccino: ₹60")
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ₹{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_rupees()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
