'''2. Write a program to implement a stack for these book-details (book no, book name). That 
is, now each item  node of the stack contains two types of information –a book no and its name. 
Just implemented push and display operations.'''
def create_book(book_no, book_name):
    return {"book_no": book_no, "book_name": book_name}

def push(stack, book_no, book_name):
    book = create_book(book_no, book_name)
    stack.append(book)
    print("Book '" + book_name + "' pushed onto the stack.")

def display(stack):
    if not stack:
        print("Stack is empty.")
    else:
        print("Books in the stack:")
        for book in reversed(stack):
            print("Book No: " + str(book["book_no"]) + ", Book Name: '" + book["book_name"] + "'")


book_stack = []
push(book_stack, 1, "To Kill a Mockingbird")
push(book_stack, 2, "1984")
display(book_stack)
