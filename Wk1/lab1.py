import math

##Problem 1

r = 5
A = math.pi * 5**2
print(A)
v = (4/3)*math.pi * r**3
print(v)
c_sq= 3**2 + 4**2
c= math.sqrt(c_sq)
print(c)

##Problem 2

name = "Reggie Brown"
length = len(name)
first_name = "Reggie"
last_name = "Brown"
full_name = first_name + " " + last_name
print(length, full_name, name.upper(), name.lower())

##Problem 3

age = 12
height = 8
weight = 460
print(type(age),type(height),type(weight))
bmi = (weight/(height*12)**2)*703
print(bmi)

