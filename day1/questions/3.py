'''The math module in Python provides mathematical functions and constants, 
allowing you to perform various mathematical operations..In this particular program, 
the math.pi constant is used to represent the mathematical constant π (pi), which is 
approximately equal to 3.14159.'''

import math

# Prompt the user to input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * radius ** 2

# Display the area of the circle
print("The area of the circle is:", area)
