# Get input from the user
num = int(input("Enter a number: "))

# Initialize variables
sum_of_numbers = 0
i = 1

# Calculate sum using a while loop
while i <= num:
    sum_of_numbers += i
    i += 1

# Print the sum
print("The sum of all numbers from 1 to",num, " is:", sum_of_numbers)
