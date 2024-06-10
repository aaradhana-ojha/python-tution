'''Write a Python program that accepts a string from user. Your program should create
and display a new string where the first and last characters have been exchanged.
For example if the user enters the string 'HELLO' then new string would be 'OELLH'.'''

# Get input from the user
user_input = input("Enter a string: ")

# Check if the string has more than one character
'''This line checks if the length of user_input is greater than 1. The len() function 
returns the length of the string.
If the length is greater than 1, the condition is True and the code inside the if block will execute.
If the length is 1 or less, the condition is False and the code inside the else block will execute.'''
if len(user_input) > 1:
    # Create a new string with the first and last characters swapped
    new_string = user_input[-1] + user_input[1:-1] + user_input[0]
    '''This line creates a new string called new_string. (hello, oellh)
user_input[-1] retrieves the last character of the string.
user_input[1:-1] retrieves all characters of the string except the first and last ones.
user_input[0] retrieves the first character of the string.
These three parts are concatenated (+ operator) to form the new string with the first and last characters swapped.'''
else:
    # If the string has one or no characters, it remains the same
    new_string = user_input

# Display the result
print("New string:", new_string)
