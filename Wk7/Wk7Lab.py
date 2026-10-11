#PART 1

def vigenere_header(alphabet):
    alpha_len = len(alphabet)
    print('|   ', end='')
    for i in range(alpha_len):
        print(f"| {alphabet[i % alpha_len]}", end=' ')
    print("|")
    print('|---'*(alpha_len+1)+'|')

def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    vigenere_header(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")


alphabet = 'abcdefghijklmnopqrstuvwxyz'

#vigenere_sq(alphabet)
#vigenere_sq('abcde')

#PART 2

def letter_to_index(letter, alphabet:str):
    return alphabet.lower().index(letter.lower())

print(letter_to_index('b', alphabet))

def index_to_letter(index, alphabet:str):
    for i,l in enumerate(alphabet):
        if i == index:
            return l

print(index_to_letter(5, alphabet))

def vigenere_index(key_letter, plain_letter, alphabet:str):
    return (letter_to_index(key_letter, alphabet) + letter_to_index(plain_letter, alphabet)) % len(alphabet)

key = 'bluesmurf'
message = "hello world, I am here"

print(vigenere_index('b','h', alphabet))

def encrypt_vigenere(key, plaintext, alphabet):
    cipter_text = ''
    for i, c in enumerate(plaintext):
        if c == ' ':
            pass
        elif (c.lower() in alphabet):
            cipher_text += index_to_letter(key[i % len(key]), alphabet), c, alphabet
        print(f'{c} ')

print(index_to_index(vigenere_index('b','h', alphabet), alphabet))