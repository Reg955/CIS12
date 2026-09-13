


def repeat(text, number):
    for i in range(number):
        print(text)

repeat("Hello", 3)

#2
def repeat(text, number):
    count = 0

    while count < number:
        print(text)
        count += 1

repeat("Hello", 3)


def print_right1(text, spaces=40):
    spaces -= len(text)
    ws = ""
    while spaces > 0:
        ws += ' '
        spaces -= 1
    print(ws + text)

print_right1("Hello")