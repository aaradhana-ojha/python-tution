# Prompt the user to enter a number and convert the input into an integer
num = int(input("Enter a number: ")) 

# Initialize variables
factorial = 1
i = 1

# Calculate the factorial using a while loop in the code using i
while i <= num:
    factorial *= i
    i += 1

# Print the factorial of the input number
print("The factorial of", num, "is:", factorial)


