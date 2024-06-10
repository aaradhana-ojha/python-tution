'''1. Write a  function in python to create a text file myfile.txt and save the content in it and 
define a function to  read the content from a text file "myfile.txt" and display the same on 
screen.  '''

def write_to_file():
    with open('myfile.txt', 'w') as file:
        file.write("Hello, this is a simple text file.")

def read_from_file():
    with open('myfile.txt', 'r') as file:
        content = file.read()
        print(content)

# Create and save content to myfile.txt
write_to_file()

# Read and display the content from myfile.txt
read_from_file()
