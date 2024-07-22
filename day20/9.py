'''Add Book: Write a function AddBook(stack, book) that adds a book (a list containing Title, Author, and Price) to the stack if the price is greater than 500.
Remove Book: Write a function RemoveBook(stack) that removes and returns the top book from the stack and displays its details. If the stack is empty, display an underflow message.'''

def AddBook(stack, book):
    if book[2] > 500:
        stack.append(book)
        print("Book '" + book[0] + "' by " + book[1] + " added to stack.")
    else:
        print("Book '" + book[0] + "' by " + book[1] + " has a price less than or equal to 500 and was not added to the stack.")

def RemoveBook(stack):
    if len(stack) == 0:
        print("Stack is empty. Underflow condition.")
    else:
        removed_book = stack.pop()
        print("Removed book: " + str(removed_book))

library_stack = []

books = [
    ["The Great Gatsby", "F. Scott Fitzgerald", 600],
    ["1984", "George Orwell", 300],
    ["To Kill a Mockingbird", "Harper Lee", 800],
    ["The Catcher in the Rye", "J.D. Salinger", 400]
]

for book in books:
    AddBook(library_stack, book)

RemoveBook(library_stack)
RemoveBook(library_stack)
RemoveBook(library_stack)
RemoveBook(library_stack)
