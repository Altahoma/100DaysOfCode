import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
gamer_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer_choice = random.randint(0, 2)

print('You chose:\n' + rps[gamer_choice])
print('Computer chose:\n' + rps[computer_choice])

if gamer_choice == computer_choice:
    print('It\'s a draw ¯\_(ツ)_/¯' )
elif gamer_choice == 2 and computer_choice == 1:
    print('You win!')
elif gamer_choice == 1 and computer_choice == 0:
    print('You win!')
elif gamer_choice == 0 and computer_choice == 2:
    print('You win!')
else:
    print('You lose :(')
