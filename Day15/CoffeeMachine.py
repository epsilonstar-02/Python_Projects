RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

RECIPES = {
    "espresso": [50, 0, 18, 1.5],
    "latte": [200, 150, 24, 2.5],
    "cappuccino": [250, 100, 24, 3.0]
}

def report():
    for i in RESOURCES:
        print(f"{i.title()}: {RESOURCES[i]}")

def money(q,d,n,p,order):
    money = q*0.25 + d*0.10 + n*0.05 + p*0.01
    change = money - RECIPES[order][3]
    if change > 0:
        RESOURCES['money'] += money - change
    elif change == 0:
        RESOURCES['money'] += money
    else:
        print("Insufficient Money!!")
        print(f"Here's your money back: ${money}")
    return change

def coffee(order, money):
    resource_names = list(RESOURCES.keys())[:-1]
    recipe_amounts = RECIPES[order][:3]
    for name, amount in zip(resource_names, recipe_amounts):
        if RESOURCES[name] < amount:
            print("Insufficient Resources!!")
            print(f"Here's your money back: ${money}")
            return
    for name, amount in zip(resource_names, recipe_amounts):
        RESOURCES[name] -= amount
    print(f"Here's your {order}!!!")

def main():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "report":
            report()
            continue
        if order not in RECIPES:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")
            continue
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
        except ValueError:
            print("Invalid input for coins. Transaction cancelled.")
            continue
        change = money(quarters, dimes, nickels, pennies, order)
        if change < 0:
            continue
        if change > 0:
            print(f"Here is ${round(change,2)} in change.")
        coffee(order, quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01)
        again = input("Would you like another coffee? (y/n): ").lower()
        if again != 'y':
            print("Thank you for using the Coffee Machine!")
            break

if __name__ == "__main__":
    main()