from sys import exit

def vigenere_header(alphabet):
    return list(' ') + list(alphabet)

def vigenere_sq(alphabet):
    alphabet = list(alphabet)
    sq_list = [vigenere_header(alphabet)]
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

def vigenere_sq_print(sq_list):
    for i,row in enumerate(sq_list):
        print(f"| {' | '.join(row)} |")
        if i == 0:
            print(f"{"|---"*len(row)}|")

def letter_to_index(letter, alphabet):
    return alphabet.upper().find(letter.upper())

def index_to_letter(index, alphabet):
    if 0 <= index < len(alphabet):
        return alphabet[index].lower()

def vigenere_index(key_letter, plaintext_letter, alphabet):
    return index_to_letter(
        (letter_to_index(plaintext_letter, alphabet) +
        letter_to_index(key_letter, alphabet)) % len(alphabet), alphabet)

def non_vigenere(key_letter, cipher_text, alphabet):
    return index_to_letter(
        (letter_to_index(cipher_text, alphabet) -
         letter_to_index(key_letter, alphabet)) % len(alphabet), alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = ''
    counter = 0
    for c in plaintext.lower():
        if c == ' ':
            cipher_text += ' '
        elif c in alphabet:
            cipher_text += vigenere_index(key[counter % len(key)], c, alphabet)
            counter += 1
    return cipher_text

def decrypt_vigenere(key, cipher_text, alphabet):
    plaintext = []
    counter = 0
    for c in cipher_text:
        if c == ' ':
            plaintext.append(' ')
        elif c in alphabet:
            plaintext.append(non_vigenere(key[counter % len(key)], c, alphabet))
            counter += 1
    return ''.join(plaintext)

def enc_menu(key, alphabet, encrypted_list):
    plaintext = input("Enter text to encrypt: ")
    encrypted_list.append(encrypt_vigenere(key, plaintext, alphabet))


def dec_menu(key, alphabet, encrypted_list):
    for cipher_text in encrypted_list:
        print(decrypt_vigenere(key, cipher_text, alphabet))


def dec_dump_menu(encrypted_list):
    print(len(encrypted_list))
    for cipher_text in encrypted_list:
        print(cipher_text)

def main():
    key = 'bluesmurf'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #message = 'Print this message for fun'
    #ct = encrypt_vigenere(key, message, alphabet)
    encrypted_list = []

    menu = [
        ['1) Encrypt', enc_menu, [key, alphabet, encrypted_list]],
        ['2) Decrypt', dec_menu, [key, alphabet, encrypted_list]],
        ['3) Dump Decrypt', dec_dump_menu, [encrypted_list]],
        ['4) Quit', exit, [0]]
    ]
    while True:
        print("-"*80)
        for menu_item in menu:
            print(menu_item[0])
        try:
            choice = int(input("Enter choice: "))
            if not (0 < choice <= len(menu)):
                print("Invalid choice")
            else:
                menu[choice-1][1](*menu[choice-1][2])
        except ValueError as ignored:
            print("Invalid choice.  Enter number between 1 and 4")

        ###menu[0][1](*menu[0][2])

#print(vigenere_index('b', 'b', alphabet))
#print(ct)
#print(decrypt_vigenere(key, ct, alphabet))
#vigenere_sq_print(vigenere_sq(alphabet))

if __name__ == '__main__':
    main()
