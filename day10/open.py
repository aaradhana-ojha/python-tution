'''In Python, you can open and close files using the open() 
function to open a file and the close() method to close it. 
It's also good practice to use the with statement when working 
with files, as it ensures that the file is properly closed after 
its suite finishes, even if an exception is raised. '''

# Open a file
with open('example.txt', 'r') as file:
    # Perform operations on the file
    content = file.read()
    print(content)
# Close the file
file.close()


# File is automatically closed when exiting the 'with' block
