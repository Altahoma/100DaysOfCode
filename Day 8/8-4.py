alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    encrypted_text = ''
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = index + shift
        if shifted_index >= 26:
            shifted_index -= 26
        encrypted_text += alphabet[shifted_index]
    print(f'The encoded text is {encrypted_text}')


def decrypt(text, shift):
    decrypted_text = ''
    for letter in text:
        index = alphabet.index(letter)
        shifted_index = index - shift
        decrypted_text += alphabet[shifted_index]
    print(f'The decoded text is {decrypted_text}')


if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
