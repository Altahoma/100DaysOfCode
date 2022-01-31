from data import MENU, resources


def check_resources(choice):
    enough_resources = True
    for item in MENU[choice]['ingredients']:
        if resources[item] < MENU[choice]['ingredients'][item]:
            print(f'Sorry there is not enough {item}.')
            enough_resources = False
    return enough_resources


def make_payment(choice):
    enough_money = False
    price = MENU[choice]['cost']
    print(f'Please insert coins, {choice} costs ${price}')
    quarters = int(input('How many quarters = $0.25?: ')) * 0.25
    dimes = int(input('How many dimes = $0.10?: ')) * 0.10
    nickles = int(input('How many nickles = $0.05?: ')) * 0.05
    pennies = int(input('How many pennies = $0.01?: ')) * 0.01
    money_inserted = quarters + dimes + nickles + pennies
    if price > money_inserted:
        print(f'Sorry that\'s not enough money. ${money_inserted} refunded.')
    else:
        enough_money = True
        resources['money'] += price
        change = round(money_inserted-price, 2)
        print(f'Here is ${change} in change.')
    return enough_money


def make_coffee(choice):
    for item in MENU[choice]['ingredients']:
        resources[item] -= MENU[choice]['ingredients'][item]
    print(f'Here is your {choice}. Enjoy!')


machine_turn = True
while machine_turn:
    option = input('    What would you like? (espresso/latte/cappuccino): ')
    if option == 'espresso' or option == 'latte' or option == 'cappuccino':
        if check_resources(option):
            if make_payment(option):
                make_coffee(option)
    elif option == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${resources["money"]}')
        pass
    elif option == 'off':
        print('Coffee machine power-off!')
        machine_turn = False
