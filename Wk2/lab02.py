#Part 1
#1
name = "Reggie"
age = 70
height = 5.7
favorite_color = "Green"
#2
#2.1
print(name)
print(age)
print(height)
print(favorite_color)
#2.2
print(name,age,height,favorite_color)
# yes the print statement adds spaces
#2.3
print(f"My name is {name} and I am {age} years old and my favorite color is {favorite_color}")
#2.4
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite color: {favorite_color}""")
# extra spaces translate through to the console
#3
import math as math
r = 5
circle_area = (math.pi * r**2)
print(round(circle_area, 1))
#Part 2
x = math.sqrt(age)
print(x)
print(math.sin(height))
print(math.cos(height))


