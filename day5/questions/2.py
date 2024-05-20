def power_numbers(a, b):
    return a ** b

# Taking input from the user
num1 = float(input("Enter the base number: "))
num2 = float(input("Enter the exponent: "))

# Performing the operation
power_result = power_numbers(num1, num2)

# Printing the result
print(num1, "raised to the power of", num2, "is", power_result)
