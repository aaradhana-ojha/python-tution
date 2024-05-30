''' A palindrome is a string that reads the same backward as forward. For example, the 
words dad, madam and radar are all palindromes. Write a programs that determines 
whether the string is a palindrome. '''

# Get input from the user
user_input = input("Enter a string: ")

# Convert the string to lowercase to ensure case-insensitive comparison
normalized_string = user_input.lower()

# Check if the string is the same forward and backward
if normalized_string == normalized_string[::-1]:
    '''This line compares the string with its reverse. 
    normalized_string[::-1] creates a reversed version of the string.'''
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
