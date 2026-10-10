#Exercise 1

def is_palindromic(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindromic('rabbit'))
print(is_palindromic('noon'))

