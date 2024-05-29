total_sum = 0

for num in range(1, 51):
    if num % 2 == 0:
        continue  # Skip even numbers
    if num % 7 == 0:
        break  # Stop the loop when a multiple of 7 is encountered
    total_sum += num  # Add the odd number to the sum

print("The sum of odd numbers until a multiple of 7 is encountered is:", total_sum)

'''Explanation:
Initialization:
Initialize a variable total_sum to 0 to keep track of the sum of odd numbers.
Loop through numbers:
Use a for loop to iterate through numbers from 1 to 50.
Skip even numbers:
Use the continue statement to skip even numbers.
Break at multiples of 7:
Use the break statement to exit the loop when a multiple of 7 is encountered.
Sum odd numbers:
Add the current number to total_sum if it is an odd number and not a multiple of 7.
Print the result:
Print the total sum of the odd numbers encountered before the loop stops.'''