# Prompt the user to enter a number and convert the input into an integer
num = int(input("Enter a number: "))

# Initialize a variable to store the sum of numbers
total_sum = 0

# Loop through numbers from 1 to the entered number inclusive
for i in range(1, num + 1):
    # Add the current number (i) to the sum
    total_sum += i

# Print the sum of numbers from 1 to the entered number
print("The sum of numbers from 1 to", num, "is:", total_sum)

'''If you provide 3 as the input, the loop will iterate over numbers from 1 to 3,
inclusive. During each iteration, the variable i will take on the value of the 
current number in the sequence. So, when num is 3, the loop will iterate with i 
taking on the values 1, 2, and 3 successively.'''