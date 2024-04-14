from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()
# menuItem = MenuItem()

#moneyMachine.report()   # Calling the method
#coffeeMaker.report()

while True:
    options = menu.get_items() # Option of a beverage
    choice = input(f"What beverage would you like? ({options}): ")
    if choice == 'off':
        break
    elif choice == 'report':
        moneyMachine.report() # Incorporation the reporting behaviour into this choice
        coffeeMaker.report()
    else:
        beverage = menu.find_drink(choice) # Searches the menu for a particular drink by name.
        print(beverage)  # Prints out a MenuItem class object
        #print(beverage.ingredients['water'])
        if coffeeMaker.is_resource_sufficient(beverage):
            if moneyMachine.make_payment(beverage.cost):
                coffeeMaker.make_coffee(beverage)
