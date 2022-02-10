numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = 'Angela'
new_list = [letter for letter in name]
print(new_list)

number_list = [num * 2 for num in range(1, 5)]
print(number_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
names_upper = [name.upper() for name in names if len(name) > 5]
print(names_upper)
