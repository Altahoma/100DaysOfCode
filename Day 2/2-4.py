print('Welcome to the tip calculator.')
bill = float(input('What was total bill? $'))
percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))
result = (bill + bill / 100 * percentage) / people
print('Each person should pay: ${:.2f}'.format(result))
