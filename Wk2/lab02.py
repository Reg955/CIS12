#Part 1
print("Part 1")
#1
name = "Reggie"
age = 854
height = 5.777777777
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
print(f"My name is {name} and I am {age:05d} years old, my height is {height:.2f} and my favorite color is {favorite_color}")
#2.4
print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite color: {favorite_color}""")
# extra spaces translate through to the console
#3
import math
r = 5
circle_area = (math.pi * r**2)
print(round(circle_area, 1))
#Part 2
print("Part 2")
x = math.sqrt(age)
print(f"sqrt of age: {x}")
print(f"sin of height {math.sin(height)}")
print(math.cos(height))
#Part 3
print("Part 3")
# The sum of age and 5.
age_plus = age + 5
# The difference between height and 4.
h_minus = height - 4
# The product of age and height.
ah_product = age * height
# The quotient of height and 2.
quo_height = height / 2
# The remainder of age divided by 3.
remainder_age = age % 3
# age raised to the power of 2.
age_sq = age ** 2

print(f"In 5 years I'll be {age_plus}")
print(f"my height-4 is: {h_minus}")
print(f"this number, {ah_product}, is age x height")
print(quo_height)
print(f"this is the remainder of age divided by 3-- {remainder_age}")
print(age_sq)
#Part 4
print("Part 4")
temp_F = int(input("Enter temperature in Farenheit: "))
temp_C = (temp_F - 32) * 5/9
print(f"The temperature in Celsius is {temp_C}°C")




