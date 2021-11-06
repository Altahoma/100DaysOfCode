from art import logo


def caesar(direction, text, shift):
    result = ''
    if shift > 26:
        shift %= 26
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            shifted_index = index + shift
            result += alphabet[shifted_index]
        else:
            result += letter
    print(f'Here\'s the {direction}d result: {result}')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

should_continue = 'yes'
while should_continue == 'yes':
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    text = input('Type your message:\n').lower()
    shift = int(input('Type the shift number:\n'))
    caesar(direction, text, shift)
    should_continue = input('Type "yes" is you want to go again. Otherwise type "no".\n').lower()

print('Goodbye!')
