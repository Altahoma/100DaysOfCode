# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# with open('my_file.txt', 'a') as file:
#     file.write('\nI am 12 years old.')

# with open('new_file.txt', 'w') as file:
#     file.write('New text.')

# with open('/Users/altahoma/Desktop/new_file_2.txt') as file:
#     contents = file.read()
#     print(contents)

with open('../../../Desktop/new_file_2.txt') as file:
    contents = file.read()
    print(contents)
