'''Write a Python program that opens a text file named "data.txt" 
in read mode, moves the file cursor to the 10th character, reads 
and prints the content from that position to the end of the file.'''

with open("data.txt", "w") as file:
    
    file.write("This is some sample text.\nIt starts from the 10th character.")

with open("data.txt", "r") as file:
    
    file.seek(9)
    content = file.read()
    print("Content from the 10th character to the end of the file:")
    print(content)
