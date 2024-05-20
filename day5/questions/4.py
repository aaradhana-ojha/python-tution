def absolute_difference(a, b):
    return abs(a - b)

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Performing the operation
absolute_difference_result = absolute_difference(num1, num2)

# Printing the result
print("The absolute difference between " ,num1, " and ", num2,  " is ", absolute_difference_result)
