from main import MENU, resources
import math

money = 0

quarters = 0.25
dimes = 0.1
nickles = 0.05
pennies = 0.01

def calculatingMoney(command_option):
    global quarters, dimes, nickles, pennies, money
    print("Please insert coins")

    total_price = 0
    the_number_of_quarters = int(input("How many quarters? : "))
    the_number_of_dimes = int(input("How many dimes? : "))
    the_number_of_nickles = int(input("How many nickles? : "))
    the_number_of_pennies = int(input("How many pennies? : "))

    total_price = the_number_of_quarters * quarters + the_number_of_dimes * dimes + the_number_of_nickles * nickles + the_number_of_pennies * pennies

    if total_price < MENU[command_option]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        
        for option in MENU[command_option]["ingredients"]:
            resources[option] -= MENU[command_option]["ingredients"][option]    

        CHANGE = round(total_price - MENU[command_option]["cost"], 3)
        money += MENU[command_option]["cost"]
        print(f"Here is ${CHANGE} in change. Here is your {command_option} ☕️. Enjoy!")

def checkResources(command_option):
    for options in MENU[command_option]["ingredients"]:
        if MENU[command_option]["ingredients"][options] > resources[options]:
            print(f"Sorry there is not enough {options}.")
            return False
    return True

def workingCoffeeMachine():
    is_working = True

    while is_working:
        command_option = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if command_option == "off":
            print("Coffee Machine is turned off")
            is_working = False
        else:
            if command_option == "report":
                print(f"water : {resources['water']}ml\nmilk : {resources['milk']}ml\ncoffee : {resources['coffee']}g\nmoney : ${money}")
            
            elif command_option not in MENU:
                print("There are no available coffee options.")
            
            elif checkResources(command_option):
                calculatingMoney(command_option)
                

workingCoffeeMachine()

# 각 커피 옵션마다 필요한 물의 양, 우유의 양, 커피원두의 양을 계산하여 추출할 수 있는 커피 머신의 상태를 업데이트 해야 함