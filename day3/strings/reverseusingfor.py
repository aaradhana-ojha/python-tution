# Define a string
original_string = "hello"

# Initialize an empty string to store the reversed string
reversed_string = ""

# Iterate through the indices of the original string in reverse order
for i in range(len(original_string) - 1, -1, -1):
    reversed_string += original_string[i]

# Print the original and reversed strings
print("Original string:", original_string)
print("Reversed string:", reversed_string)
