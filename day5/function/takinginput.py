def add_numbers(a, b):
    sum = a + b
    return sum

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calling the function and printing the result
result = add_numbers(num1, num2)
print("The sum of" ,num1," and", num2, "is",result)
