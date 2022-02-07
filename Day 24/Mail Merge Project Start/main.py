with open('./Input/Letters/starting_letter.txt') as example_file:
    example = example_file.read()

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    letter = example.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_from_{name}.txt', 'w') as new_file:
        new_file.write(letter)
