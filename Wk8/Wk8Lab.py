def vigenere_sq(alphabet):
    alphabet = list(alphabet)
    sq_list = []
    for i in range(len(alphabet)):
        sq_list.append(list(alphabet[i]) + alphabet[i:] + alphabet[:i])
    return sq_list

alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(vigenere_sq(alphabet))

