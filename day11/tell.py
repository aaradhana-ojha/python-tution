'''Imagine you're reading a book and you want to know which 
page you're currently on. Similarly, tell() tells you the 
current "position" in the file, measured in bytes from the beginning.'''
with open("example.txt", "r") as file:
    print(file.tell())  # Output the current position
    data = file.read()  # Read from the current position
    print(file.tell())  # Output the updated position after reading
'''print(file.tell()): Initially, this line prints the current 
"page number," or byte offset, which is the starting position 
before reading any pages. Let's say it prints "Page 0".

part_of_story = file.read(): This line reads some pages of 
the story, in this case, the entire content of "helloworld.txt". 
Let's assume it reads the entire file, which is "Hello, World!".

print(file.tell()): After reading, this line prints the updated 
"page number," or byte offset, which reflects the new position 
after reading. Since we've read the entire file, the file cursor 
is now at the end of the file. So, it might print "Page 13" if 
"Hello, World!" contains 13 characters, including spaces and punctuation.'''