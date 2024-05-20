def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing operations
sum_result = add_numbers(num1, num2)
difference_result = subtract_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
quotient_result = divide_numbers(num1, num2)

# Printing the results
print("The sum of", num1, "and", num2, "is", sum_result)
print("The difference when", num2, "is subtracted from", num1, "is", difference_result)
print("The product of", num1, "and", num2, "is", product_result)
print("The quotient when", num1, "is divided by", num2, "is", quotient_result)
