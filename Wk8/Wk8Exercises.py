from os import getcwd
# Writing to a file
with open("greeting.txt", "w") as writer:
    writer.write("Hello, World!\nWelcome to Python programming.")

# Reading from a file
with open("greeting.txt", "r") as reader:
    for line in reader:
        print(line.strip())


#print(getcwd())
message = "Hello, World!"
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Position of 'World':", message.find("World"))
print("Replacing 'World' with 'Universe':", message.replace("World", "Universe"))

name = "python"
name_list = list(name)
