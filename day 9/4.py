'''Write a Python program that accepts a string from user. Your program should create a
new string in reverse of first string and display it.
For example if the user enters the string 'EXAM' then new string would be 'MAXE'.'''

# Get input from the user
user_input = input("Enter a string: ")

# Create a new string that is the reverse of the input string
reversed_string = user_input[::-1]

'''This line uses slicing to reverse the string.
user_input[::-1] works as follows:
user_input[start:stop:step] is the general form for slicing.
Omitting start and stop means it considers the entire string.
step of -1 means it starts from the end of the string and steps backwards.'''

# Display the reversed string
print("Reversed string:", reversed_string)
