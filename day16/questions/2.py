'''Write a program to implement a stack for these book-details 
(book no, book name). That is, now each item node of the stack 
contains two types of information –a book no and its name. Just 
implemented push and display operations.'''

class Book:
    def create_book(book_no, book_name):
        return {
            "book_no": book_no,
            "book_name": book_name
        }

    def book_repr(book):
        return "Book No: " + str(book["book_no"]) + ", Book Name: '" + book["book_name"] + "'"
    
'''Class Definition: class Book defines a class named Book. This class will be used to manage book details.

create_book Method:

Parameters: Takes book_no (an identifier for the book) and book_name (the name of the book).
Functionality: Creates and returns a dictionary representing a book with keys book_no and book_name.'''


class Stack:
    stack = []

    @staticmethod
    def push(book_no, book_name):
        book = Book.create_book(book_no, book_name)
        Stack.stack.append(book)
        print("Book '" + book_name + "' pushed onto the stack.")
        '''Class Definition: class Stack defines a class named Stack. This class will be used to manage a stack of books.

Static Attribute stack:

Functionality: This is a class-level list that will store the stack items (books).'''
        '''push Method:

Parameters: Takes book_no (an identifier for the book) and book_name (the name of the book).
Functionality: Creates a new book using the Book.create_book method and appends it to the stack list. 
It then prints a message indicating that the book has been pushed onto the stack.'''


    @staticmethod
    def display():
        if not Stack.stack:
            print("Stack is empty.")
        else:
            print("Books in the stack:")
            for book in reversed(Stack.stack):
                print(Book.book_repr(book))


# Pushing books onto the stack
Stack.push(1, "To Kill a Mockingbird")
Stack.push(2, "1984")
Stack.push(3, "The Great Gatsby")

# Displaying books in the stack
Stack.display()
