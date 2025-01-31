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

profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

def is_resource_enough(order_ingredient):
    """Checks if there are enough resources to make the drink."""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:  # Fixed condition
            print(f"🚨 SORRY, NOT ENOUGH {item.upper()}!")
            return False
    return True  # Added return True when resources are enough

def coins():
    """Returns the total money inserted by the user."""
    print("💰 Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total

def transaction_status(money, drink_cost):
    """Handles transaction logic."""
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"✅ Transaction successful! Your change is ${change}.")
        return True
    else:
        print("❌ Not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredient):
    """Deducts the used resources and makes the coffee."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"☕ Here is your {drink_name}! Enjoy! 😊")

is_on = True

while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino) or type 'report'/'off': ").lower()
    
    if choice == "off":
        is_on = False
        print("🔴 Turning off the coffee machine. Goodbye!")
    
    elif choice == "report":
        print(f"📊 Milk: {resources['milk']} ml")
        print(f"📊 Water: {resources['water']} ml")
        print(f"📊 Coffee: {resources['coffee']} g")
        print(f"📊 Money: $ {profit}")
    
    elif choice in MENU:
        drink = MENU[choice]
        
        if is_resource_enough(drink["ingredients"]):  # Check resources first
            payments = coins()  # Ask for payment
            if transaction_status(payments, drink["cost"]):  # Check transaction success
                make_coffee(choice, drink["ingredients"])  # Deduct resources and serve coffee
    
    else:
        print("⚠️ Invalid choice. Please select a valid drink!")
