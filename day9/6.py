'''Write a program that asks the user to input his name and print its initials. Assuming 
that the user always types first name, middle name and last name and does not include 
any unnecessary spaces. 
For example, if the user enters Ajay Kumar Garg the program should display A. K. G. 
Note:Don't use split() method '''

# Get input from the user
full_name = input("Enter your full name (first name, middle name, last name): ")

# Initialize an empty string to store the initials
initials = "" 

# Use a flag to identify the start of each word. This flag helps in identifying the first character of each word.
start_of_word = True
# (since the very first character of the string is the start of the first word).

#Aaradhana, ojha, aaradhana (A. O. A.)
# Iterate through each character in the full name
for char in full_name:
    if start_of_word:
        # Append the uppercase initial and a period to the initials string
        initials += char.upper() + ". "
        start_of_word = False
    # Check if the current character is a space
    if char == ' ':
        start_of_word = True
        
'''The loop iterates through each character in full_name.
If start_of_word is True, it means the current character is the start of a word. The character is converted to uppercase, followed by a period and a space, and appended to initials.
The flag start_of_word is then set to False to avoid adding a period for subsequent characters of the same word.
If a space is encountered, start_of_word is set to True to mark the start of a new word.'''

# Print the initials
print("Initials:", initials.strip())

#This line prints the initials. The strip() method is used to remove any trailing spaces from the final initials string.
