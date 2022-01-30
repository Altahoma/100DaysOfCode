from art import logo
import random


def get_card(hand):
    card = random.choice(cards)
    score = sum(hand) + card
    if card == 11 and score > 21:
        card = 1
    hand.append(card)


def start_game():
    if input('Do you want to play a game Blackjack? Type "y" or "n": ') == 'n':
        return
    player_cards = []
    dealer_cards = []
    get_card(player_cards)
    get_card(player_cards)
    get_card(dealer_cards)
    get_card(dealer_cards)
    player_score = sum(player_cards)
    dealer_score = sum(dealer_cards)

    print(f'Your cards: {player_cards}, current score: {player_score}')
    print(f'Dealer first card: {player_cards[:1]}')

    if player_score == 21:
        if dealer_score != 21:
            print(f'Your cards: {player_cards}, current score: {player_score}')
            print(f'Dealer cards: {dealer_cards}, current score: {dealer_score}')
            print('You win! :)')
            start_game()
    elif player_score < 21:
        while input('Type "y" to get another card, type "n" to pass: ') == 'y':
            get_card(player_cards)
            player_score += player_cards[-1]
            print(f'Your cards: {player_cards}, current score: {player_score}')
            if player_score < 21:
                print(f'Dealer first card: {player_cards[:1]}')
            elif player_score > 21:
                print(f'Dealer cards: {dealer_cards}, current score: {dealer_score}')
                print('You lose! :(')
                start_game()

    while dealer_score < 17:
        get_card(dealer_cards)
        dealer_score += dealer_cards[-1]

    if player_score < dealer_score <= 21:
        print(f'Your cards: {player_cards}, current score: {player_score}')
        print(f'Dealer cards: {dealer_cards}, current score: {dealer_score}')
        print('You lose! :(')

    if player_score == dealer_score:
        print(f'Your cards: {player_cards}, current score: {player_score}')
        print(f'Dealer cards: {dealer_cards}, current score: {dealer_score}')
        print('Draw!')

    if dealer_score > 21:
        print(f'Your cards: {player_cards}, current score: {player_score}')
        print(f'Dealer cards: {dealer_cards}, current score: {dealer_score}')
        print('You win! :)')

    if player_score > dealer_score:
        print(f'Your cards: {player_cards}, current score: {player_score}')
        print(f'Dealer cards: {dealer_cards}, current score: {dealer_score}')
        print('You win! :)')

    start_game()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# print(logo)
start_game()
