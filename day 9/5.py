''' Write a Python program that accepts a string from user. Your program should create a 
new string by shifting one position to left'''

# Get input from the user
user_input = input("Enter a string: ")

# Check if the string is empty or has only one character
if len(user_input) <= 1:
    shifted_string = user_input
else:
    # Create a new string by shifting one position to the left
    shifted_string = user_input[1:] + user_input[0]
    '''This line creates a new string by slicing the original 
    string from the second character to the end (user_input[1:]) HELLO -> ELLOH
    and appending the first character (user_input[0]) to the end of the slice.
user_input[1:] gets all characters of the string except the first one.
user_input[0] gets the first character of the string.'''

# Display the shifted string
print("Shifted string:", shifted_string)

'''HELLO
Reversed string: OLLEH
Shifted one position to the left: ELLOH'''
