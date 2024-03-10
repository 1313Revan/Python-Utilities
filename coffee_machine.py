# This is a project from Angela Wu's 100 Days of Code Python bootcamp

from data import MENU, resources
import sys


money = 0
esp_ingredients = {"ingredients": MENU["espresso"]["ingredients"]}
latte_ingredients = {"ingredients": MENU["latte"]["ingredients"]}
capp_ingredients = {"ingredients": MENU["cappuccino"]["ingredients"]}


def pay(drink):
    global money
    required = MENU[drink]["cost"]
    while money < required:
        print("\nPlease insert payment:\n")
        print(f"Total: ${required:.2f}\nAvailable: ${money:.2f}\n")
        payment = input(">> ").lower()
        if payment == "quarter":
            payment = 0.25
        elif payment == "dime":
            payment = 0.10
        elif payment == "nickel":
            payment = 0.05
        elif payment == "penny":
            payment = 0.01
        money += payment
    if money > required:
        print("\nWould you like your change now?\n")
        change = input(">> ").lower()
        if change == "yes":
            print("\nHere is your change...")
            print(f"Change: ${(money - required):.2f}\n")
            money = 0
        else:
            print("\nMaking your drink now.\n")
            money -= required
    if money == required:
        money = 0


def make_order(drink):
    print("\nMaking your drink...\n")
    if drink == "espresso":
        resources["water"] -= esp_ingredients["ingredients"]["water"]
        resources["coffee"] -= esp_ingredients["ingredients"]["coffee"]
    elif drink == "latte":
        resources["water"] -= latte_ingredients["ingredients"]["water"]
        resources["milk"] -= latte_ingredients["ingredients"]["milk"]
        resources["coffee"] -= latte_ingredients["ingredients"]["coffee"]
    elif drink == "cappuccino":
        resources["water"] -= capp_ingredients["ingredients"]["water"]
        resources["milk"] -= capp_ingredients["ingredients"]["milk"]
        resources["coffee"] -= capp_ingredients["ingredients"]["coffee"]
    print(f"Here is your {drink}!\n")


def order_again():
    global money
    if money > 0:
        print("\nWould you like to order anything else?\n")
        more = input(">> ").lower()
        if more == "no":
            print("\nDispensing your change...")
            print(f"Change: ${money:.2f}\n")
            money = 0
    order()


def order():
    global money
    print("\nWhat would you like?")
    print("\nEspresso\nLatte\nCappuccino\n")
    customer_order = input(">> ").lower()
    if customer_order == "espresso":
        if resources["water"] >= esp_ingredients["ingredients"]["water"] and resources["coffee"] >= \
                esp_ingredients["ingredients"]["coffee"]:
            pay("espresso")
            make_order("espresso")
            order_again()
        elif resources["water"] < esp_ingredients["ingredients"]["water"]:
            print("\nSorry, there is not enough water.\n")
            order()
        elif resources["coffee"] < esp_ingredients["ingredients"]["coffee"]:
            print("\nSorry, there is not enough coffee.\n")
            order()
    elif customer_order == "latte":
        if resources["water"] >= latte_ingredients["ingredients"]["water"] and resources["coffee"] >= \
                latte_ingredients["ingredients"]["coffee"] and resources["milk"] >= \
                latte_ingredients["ingredients"]["milk"]:
            pay("latte")
            make_order("latte")
            order_again()
        elif resources["water"] < latte_ingredients["ingredients"]["water"]:
            print("\nSorry, there is not enough water.\n")
            order()
        elif resources["milk"] < latte_ingredients["ingredients"]["milk"]:
            print("\nSorry, there is not enough milk.\n")
            order()
        elif resources["coffee"] < latte_ingredients["ingredients"]["coffee"]:
            print("\nSorry, there is not enough coffee.\n")
            order()
    elif customer_order == "cappuccino":
        if resources["water"] >= capp_ingredients["ingredients"]["water"] and resources["coffee"] >= \
                capp_ingredients["ingredients"]["coffee"] and resources["milk"] >= \
                capp_ingredients["ingredients"]["milk"]:
            pay("cappuccino")
            make_order("cappuccino")
            order_again()
        elif resources["water"] < capp_ingredients["ingredients"]["water"]:
            print("\nSorry, there is not enough water.\n")
            order()
        elif resources["milk"] < capp_ingredients["ingredients"]["milk"]:
            print("\nSorry, there is not enough milk.\n")
            order()
        elif resources["coffee"] < capp_ingredients["ingredients"]["coffee"]:
            print("\nSorry, there is not enough coffee.\n")
            order()
    elif customer_order == "report":
        print(f"\nWater: {resources["water"]}ml\nMilk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g\nMoney: ${money:.2f}\n")
        input()
        order()
    elif customer_order == "refill":
        print("\nWater\nMilk\nCoffee\n")
        fill = input(">> ")
        if fill == "all":
            resources["water"] = 300
            resources["milk"] = 200
            resources["coffee"] = 100
        elif fill == "water":
            resources["water"] = 300
        elif fill == "milk":
            resources["milk"] = 200
        elif fill == "coffee":
            resources["coffee"] = 100
        order()
    elif customer_order == "off":
        sys.exit()
    else:
        print("\nPlease choose one of the available options.\n")
        order()


order()
