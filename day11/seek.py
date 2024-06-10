'''In Python, seek() and tell() are methods used for handling file operations.

seek(offset, whence): This method is used to change the current file position. 
The offset argument specifies the number of bytes to move, and the whence 
argument specifies the reference point for the offset. Possible values for whence are:

0 (default): Beginning of the file
1: Current file position
2: End of the file'''

'''Imagine you have a big book with lots of pages, 
like a novel. When you read the book, you start from 
the first page and go page by page until you reach the end.

Now, the seek() function in Python is like being able to 
flip to any page you want without having to go through all 
the pages in between. Here's how it works:

seek(offset, whence):
offset means how many pages you want to move. If it's positive, 
you move forward; if it's negative, you move backward.
whence tells Python where to start counting from:
If it's 0, you start counting from the beginning of the book.
If it's 1, you start counting from where you are currently.
If it's 2, you start counting from the end of the book.
So, when you use seek(), you're like a super-fast reader who can jump to any page in the book instantly!'''

with open("example.txt", "r") as file:
    file.seek(5)  # Move to the 6th byte from the beginning of the file
    data = file.read()
    print(data)

'''Imagine "example.txt" is our book. We're opening it and starting to read. 
Now, with file.seek(5), we're saying, "Hey, let's skip ahead to the 6th byte (or character) in the book."

Here:

The "example.txt" file is like our book.
file.seek(5) is like saying, "Go to the 6th byte (or character) of the file."
data = file.read() means we start reading from that point onwards.
Finally, print(data) displays what we read.
So, with seek(5), we're jumping ahead to the 6th byte in the file and then reading from there.'''