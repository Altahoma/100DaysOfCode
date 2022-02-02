from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_turn = True
while machine_turn:
    option = menu.get_items()
    choice = input(f'    What would you like? ({option}): ')

    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print('Coffee machine power-off!')
        machine_turn = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
