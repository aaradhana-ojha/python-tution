def modulus_numbers(a, b):
    return a % b

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing the operation
modulus_result = modulus_numbers(num1, num2)

# Printing the result
print("The remainder when",num1, "is divided by", num2, "is", modulus_result)
