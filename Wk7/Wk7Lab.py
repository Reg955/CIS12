def vigenere_sq(alphabet):
    alpha_len = len(alphabet)
    for shift in range(alpha_len):
        for i in range(alpha_len):
            if i == 0:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
            else:
                print(f"| {alphabet[(i + shift) % alpha_len]}", end=' ')
        print("|")


alphabet = 'abcdefghijklmnopqrstuvwxyz'

vigenere_sq(alphabet)