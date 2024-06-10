# Open a file
file = open('example.txt', 'r')

# Properties
print("Name:", file.name)
print("Mode:", file.mode)
print("Closed:", file.closed)

# Methods
content = file.read()  # Read the entire file
print("Content:", content)

file.close()  # Close the file
print("Closed:", file.closed)