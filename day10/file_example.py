# Writing to a text file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    
    
    

# Reading from a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)

'''with open('example.txt', 'r') as file:: Opens the file example.txt in read mode ('r').
content = file.read(): Reads the entire content of the file into the variable content.
print(content): Prints the content of the file.'''

# Reading lines
with open('example.txt', 'r') as file:
    lines = file.readlines()
    print("Lines of the file:")
    print(lines)
    
'''with open('example.txt', 'r') as file:: Opens the file example.txt in read mode ('r').
lines = file.readlines(): Reads all lines of the file into a list, where each element is a line from the file.
print(lines): Prints the list of lines.'''

