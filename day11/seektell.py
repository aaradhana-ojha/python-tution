# Open the file in read mode
with open("example1.txt", "r") as file:
    # Print the current position in the file
    print("Current position in file:", file.tell())

    # Move to a specific position in the file
    file.seek(5)

    # Print the new position in the file after seeking
    print("Position after seeking:", file.tell())

    # Read and print the content from the current position
    content = file.read()
    print("Content from current position:", content)

    # Print the final position in the file after reading
    print("Final position in file:", file.tell())
'''Open the file "example1.txt" in read mode.
Print the current position in the file using tell().
Move the file cursor to the 6th byte (or character) using seek(5).
Print the new position in the file after seeking.
Read and print the content from the current position.
Print the final position in the file after reading.'''


'''Think of a file as a book, and each character in the file is like a letter or word in that book.
When you open the file, it's like opening the book and seeing the first page. At this point, you're at the beginning of the book, just like when you start reading from the first page.
Now, let's say you want to start reading from the 6th page of the book instead of the first page. That's when you use file.seek(5) to jump to the 6th page.
After jumping to the 6th page, you start reading from there using file.read(). You read until the end of the book, just like when you keep reading until you finish the chapter.
If there's a big title at the beginning of the 6th page, like "Chapter 6: Adventure Begins", that title is part of what you read. Similarly, if there's a newline character at the beginning of the 6th page in the file, it's also part of what you read.
Finally, after finishing reading, you want to know which page you're on now. That's when you use file.tell() to find out your new position in the book.'''