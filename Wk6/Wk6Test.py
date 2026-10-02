minutes = 145
#hours, minutes = divmod(minutes, 60)
#print(f'{hours} hours and {minutes} minutes')
result = divmod(minutes, 60)
print(type(result))
print(result)

def repeat(word, n):
    print(word * n)

result = repeat('Python, ', 3)
print(f"The return value is: {result}")

def repeat_string(word, n):
    return word * n

line = repeat_string('Python, ', 3)
print(f"Repeated string: {line}")

