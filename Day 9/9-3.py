from replit import clear
from art import logo


def add_bidder(bidders_list):
    name = input('What\'s your name?: ')
    bid = int(input('What\'s your bid?: $'))
    bidders_list[name] = bid


def find_winner(bidders_list):
    winner = ''
    max_bid = 0
    for name, bid in bidders_list.items():
        if bid > max_bid:
            max_bid = bid
            winner = name
    print(f'The winner is {winner} with a bid of ${max_bid}.')


print(logo)
print('Welcome to the secret auction program')
bidders = {}

should_continue = 'yes'
while should_continue == 'yes':
    add_bidder(bidders)
    should_continue = input('Are there any other bidders? Type "yes" or "no".\n').lower()
    clear()

find_winner(bidders)
