# Prompt the user to enter a positive integer
while True:
    num = int(input("Enter a positive integer: "))
    if num > 0:
        break  # Exit the loop if a positive integer is entered
    else:
        print("Please enter a valid positive integer.")

'''This block of code continuously prompts the user to enter a positive integer until a valid positive 
integer is entered.
It uses a while loop with the condition True to repeatedly ask for input.
Inside the loop, the user input is converted to an integer using int().
If the entered number is greater than 0, the loop breaks, and the program continues. 
Otherwise, it prints a message asking the user to enter a valid positive integer.'''

# Initialize variables
sum_even = 0
current_num = 2  # Start checking from 2
'''Here, we initialize two variables: sum_even to store the sum of even numbers, 
and current_num to keep track of the current number being evaluated, starting from 
2 since we're looking for even numbers.'''


# Calculate the sum of even numbers from 2 to num
while current_num <= num:
    sum_even += current_num
    current_num += 2  # Move to the next even number
'''This while loop calculates the sum of even numbers from 2 to the entered positive integer (num).
Inside the loop, sum_even is incremented by current_num, which represents the current even number.
After adding the current even number to the sum, current_num is incremented by 2 to move to the next even number.'''

# Print the sum of even numbers
print("The sum of even numbers from 2 to", num, "is:", sum_even)
