# Ask the user to enter a number
n = int(input("Enter a number: ")) 

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, n+1):
    factorial =factorial* i

# Print the factorial
print("The factorial of",n," is:", factorial)
