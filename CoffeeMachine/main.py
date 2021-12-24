# TODO: 1) Leave espresso & milk out of the functionality for now & write rest of it.


from resources import MENU, resources


def print_report(data):
    """Prints Available Machine Resources"""
    water = data["water"]
    milk = data["milk"]
    coffee = data["coffee"]
    money = data["money"]
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"


def update_resources(machine_resources, item_resources):
    """Updates resources of machine after an action is performed"""
    machine_resources["water"] = machine_resources["water"] - item_resources["ingredients"]["water"]
    machine_resources["coffee"] = machine_resources["coffee"] - item_resources["ingredients"]["coffee"]
    machine_resources["milk"] = machine_resources["milk"] - item_resources["ingredients"]["milk"]


def check_resources(item_resources):
    """Check if machine has available resources to make coffee"""
    for item in item_resources:
        if item_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def check_for_coins(drinkcost):
    """Calculates value of coins & checks if sufficient amount is entered."""
    quaters = float(input("Number of Quaters: "))
    dimes = float(input("Number of Dimes: "))
    nickels = float(input("Number of Nickles: "))
    pennies = float(input("Number of Pennies: "))
    money = round((quaters*0.25) + (dimes*0.10) + (nickels*0.05) + (pennies*0.01), 2)
    if money > (1.5 * drinkcost["cost"]):
        change = round(money - drinkcost["cost"], 2)
        print(money, change)
        print(f"Here is ${change} in change.")
    elif drinkcost["cost"] > money:
        print("Sorry that's not enough money. Money Refunded.")
        return False
    else:
        resources["money"] += money
        resources["money"] = round(resources["money"] - drinkcost["cost"], 2)
    return True


should_continue = True


while should_continue:
    function = input("What would you like? (espresso/latte/cappuccino):")
    if function == "report":
        print(print_report(resources))
    elif function == "off":
        should_continue = False
    else:
        # drink = MENU[function]
        # print(check_resources(drink["ingredients"]))
        drink = MENU[function]
        if check_resources(drink["ingredients"]):
            if check_for_coins(MENU[function]):
                update_resources(resources, MENU[function])
                print(f"Here is your {function}")
