'''. A text file named "matter.txt" contains some text, which needs to be displayed such 
that every next character is separated by a symbol "#". Write a function definition for 
hash_display() in Python that would display the entire content of the file matter.txt in the 
desired format. 
Example : 
If the file matter.txt has the following content stored in it : 
THE WORLD IS ROUND 
The function hash_display() should display the following content : 
T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#  '''

def hash_display(filename):
    # Creating the file and writing sample content for demonstration
    with open(filename, 'w') as file:
        file.write("THE WORLD IS ROUND")

    # Reading from the file and processing the content
    with open(filename, 'r') as file:
        content = file.read()
        hashed_content = "#".join(content)
        print(hashed_content)

# Use the function
hash_display('matter.txt')

