'''Write PushOn(Book) and Pop(Book) methods/functions in Python to add a new Book and 
delete a Book from a List of Book titles, considering them to act as push and pop operations of 
the Stack data structure'''

def PushOn(stack, book):
    stack.append(book)
    print("Book '" + book + "' pushed onto the stack.")
    
    '''This function takes two parameters: stack, which is a list representing our stack, and book, which is a string representing the title of the book.
It uses the append method to add the book to the end (top) of the list.
It then prints a message confirming that the book has been added to the stack.'''

def Pop(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    book = stack.pop()
    print("Book '" + book + "' popped from the stack.")
    return book

'''Define the Pop function:

This function takes one parameter: stack, which is a list representing our stack.
It first checks if the stack is empty using the not keyword. If the stack is empty, it prints a message saying that the stack is empty and that a pop operation cannot be performed, and then it returns None.
If the stack is not empty, it uses the pop method to remove the last item (top of the stack) from the list and assigns it to the variable book.
It prints a message confirming that the book has been removed from the stack.
Finally, it returns the popped book.'''

book_stack = []

PushOn(book_stack, "To Kill a Mockingbird")
PushOn(book_stack, "1984")
PushOn(book_stack, "The Great Gatsby")
PushOn(book_stack, "Moby Roy")

'''Push books onto the stack:

Use the PushOn function to add four books to the stack: "To Kill a Mockingbird", "1984", "The Great Gatsby", and "Moby Dick".
After each push operation, a message is printed to confirm the addition'''


print("Current stack:", book_stack)

Pop(book_stack)
Pop(book_stack)
Pop(book_stack)
Pop(book_stack)
Pop(book_stack) 


print("Current stack:", book_stack)
